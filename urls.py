from django.conf.urls import url, include
from rest_framework import routers

from api.views import AllListView

router = routers.DefaultRouter()
router.register(r'all', AllListView, 'all')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]