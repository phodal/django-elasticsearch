from haystack import indexes

from .models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    location = indexes.LocationField(model_attr='get_location')
    location_info = indexes.LocationField(model_attr='get_location_info')

    def get_model(self):
        return Note