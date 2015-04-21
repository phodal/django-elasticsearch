from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from mezzanine.core.views import direct_to_template
from tastypie.api import Api
from nx.api import NoteResource

apiv1 = Api(api_name='v1')
apiv1.register(NoteResource())

admin.autodiscover()

urlpatterns = i18n_patterns("",
    ("^admin/", include(admin.site.urls)),
)

urlpatterns += patterns('nx.views',
    url("^notes/$", "notes", name="note"),
)

urlpatterns += patterns('',
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    (r'^search/', include('haystack.urls')),
    url(r"^api/", include(apiv1.urls)),
    ("^", include("mezzanine.urls")),
)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
