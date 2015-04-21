from haystack import indexes

from django.utils import timezone

from .models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    location = indexes.LocationField(model_attr='get_location')

    def get_model(self):
        return Note

    @staticmethod
    def prepare_location(obj):
        try:
            return obj.location.point
        except AttributeError:
            return None

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(timestamp__lte=timezone.now())