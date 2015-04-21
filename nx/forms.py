from django.core.exceptions import ValidationError
from django.forms.models import modelform_factory
from haystack.forms import SearchForm
from nx.models import Note


class NotesSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()

BaseNoteForm = modelform_factory(Note, fields=["username", "phone_number", "title",
                                               "body", "price", "number", "latitude", "longitude"])

class NotesForm(BaseNoteForm):

    def clean(self):
        title = self.cleaned_data.get("title", None)
        body = self.cleaned_data.get("body", None)
        if not title and not body:
            raise ValidationError("Either a title or body is required")
        return self.cleaned_data
