from haystack import indexes

from .models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    number = indexes.IntegerField(model_attr='number')
    price = indexes.IntegerField(model_attr='price')
    phone_number = indexes.IntegerField(model_attr='phone_number')
    location = indexes.LocationField(model_attr='get_location')
    location_info = indexes.CharField(model_attr='get_location_info')

    def get_model(self):
        return Note