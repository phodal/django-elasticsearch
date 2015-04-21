from django.core.exceptions import ValidationError
from django.forms.models import modelform_factory
from haystack.forms import SearchForm
from nx.models import Note


class NotesSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()

BaseNoteForm = modelform_factory(Note, fields=["username", "phone_number", "title",
                                               "body", "price", "number", "province", "city", "address"])

class NotesForm(BaseNoteForm):

    def clean(self):
        title = self.cleaned_data.get("title", None)
        body = self.cleaned_data.get("body", None)
        phone_number = self.cleaned_data.get("phone_number", None)
        province = self.cleaned_data.get("province", None)
        city = self.cleaned_data.get("city", None)
        address = self.cleaned_data.get("address", None)
        if not title and not body:
            raise ValidationError("Either a title or body is required")
        if not phone_number:
            raise ValidationError("Either phone_number is required")
        if not province:
            raise ValidationError("Either province is required")
        if not city:
            raise ValidationError("Either city is required")
        if not address:
            raise ValidationError("Either address is required")
        return self.cleaned_data
