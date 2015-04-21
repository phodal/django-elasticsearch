from tastypie.paginator import Paginator
from tastypie.exceptions import BadRequest
from tastypie.resources import ModelResource
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from django.conf.urls import url

from .models import Note


class NoteResource(ModelResource):
    class Meta:
        # queryset = Note.objects.all().order_by('-created')
        queryset = Note.objects.all()
        resource_name = 'notes'

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search/?$" % (self._meta.resource_name), self.wrap_view('get_search'),
                name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        print request.GET
        query = request.GET.get('q', None)
        if not query:
            raise BadRequest('Please supply the search parameter (e.g. "/api/v1/notes/search/?q=css")')

        # results = SearchQuerySet().models(Note).filter(user=request.user).auto_query(query)
        results = SearchQuerySet().models(Note).auto_query(query)
        if not results:
            results = EmptySearchQuerySet()

        paginator = Paginator(request.GET, results, resource_uri='/api/v1/notes/search/')

        bundles = []
        for result in paginator.page()['objects']:
            bundle = self.build_bundle(obj=result.object, request=request)
            bundles.append(self.full_dehydrate(bundle))

        object_list = {
            'meta': paginator.page()['meta'],
            'objects': bundles
        }
        object_list['meta']['search_query'] = query

        self.log_throttled_access(request)
        return self.create_response(request, object_list)