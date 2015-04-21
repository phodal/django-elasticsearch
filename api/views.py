from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.template import context
from haystack.forms import ModelSearchForm
from haystack.query import EmptySearchQuerySet, SearchQuerySet
from rest_framework import generics
from api.serializer import SearchResultSerializer


class SearchView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SearchResultSerializer


    def get_queryset(self, *args, **kwargs):
        # This will return a dict of the first known
        # unit of distance found in the query
        request = self.request
        results = EmptySearchQuerySet()

        if request.GET.get('q'):
            form = ModelSearchForm(request.QUERY_PARAMS, searchqueryset=None, load_all=True)

            if form.is_valid():
                query = form.cleaned_data['q']
                results = form.search()
        else:
            form = ModelSearchForm(searchqueryset=None, load_all=True)

        if results.query.backend.include_spelling:
            context['suggestion'] = form.get_suggestion()

        distance = None
        unit = None
        try:
            k,v = ((k,v) for k,v in request.QUERY_PARAMS.items() if k in D.UNITS.keys()).next()
            distance = {k:v}
            unit = k
        except Exception as e:
            logging.error(e)

        point = None
        try:
            point = Point(float(request.QUERY_PARAMS['latitude']), float(request.QUERY_PARAMS['longitude']))
        except Exception as e:
            logging.error(e)

        if distance and point:
            results = results or SearchQuerySet()
            results = results.dwithin('location', point, D(**distance)).distance('location', point)


        return results
        #return Response(SearchResultSerializer(sqs, many=True, unit=unit).data)