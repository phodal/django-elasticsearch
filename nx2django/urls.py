from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    ("^api/", include("api.urls")),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
