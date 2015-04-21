from django.contrib.gis.measure import D

from django.shortcuts import render_to_response

from .forms import NotesSearchForm
from haystack.query import SearchQuerySet
from haystack.utils.geo import Point


def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    print notes

    center = Point(-95.23947, 38.9637903)
    max_dist = D(mi=1000)
    sqs = SearchQuerySet().dwithin('location', center, max_dist)
    print sqs
    return render_to_response('notes.html', {'notes': notes})