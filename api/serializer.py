from rest_framework import serializers


class DistanceSerializer(serializers.Serializer):
    km = serializers.FloatField()
    m = serializers.FloatField()
    mi = serializers.FloatField()
    ft = serializers.FloatField()


class SearchResultSerializer(serializers.Serializer):
    text = serializers.CharField()
    pub_date = serializers.DateTimeField()
    distance = fields.SerializerMethodField('_distance')
    content_type = fields.CharField(source='model_name')
    content_object = fields.SerializerMethodField('_content_object')

    def _content_object(self, obj):
        if obj.model_name == 'foo':
            return FoSerializer(obj.object, many=False, context=self.context).data
        if obj.model_name == 'bar':
            return BarSerializer(obj.object, many=False, context=self.context).data
        return {}

    def __init__(self,  *args, **kwargs):
        self.unit = kwargs.pop('unit', None)
        return super(SearchResultSerializer, self).__init__(*args, **kwargs)

    def _distance(self, obj):
        if self.unit:
            return {self.unit: getattr(obj.distance, self.unit)}
        try:
            return DistanceSerializer(obj.distance, many=False).data
        except Exception as e:
            ## Log this
            return {}