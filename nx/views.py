from django.shortcuts import render_to_response
from django.views.generic import CreateView

from .forms import NotesSearchForm, NotesForm

from nx.models import Note


def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    return render_to_response('notes.html', {'notes': notes})

class NoteCreate(CreateView):
    """
    Link creation view - assigns the user to the new link, as well
    as setting Mezzanine's ``gen_description`` attribute to ``False``,
    so that we can provide our own descriptions.
    """

    form_class = NotesForm
    model = Note
