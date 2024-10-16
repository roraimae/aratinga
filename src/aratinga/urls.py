from django.urls import include
from django.urls import path
from django.urls import re_path
from wagtail import urls as wagtailcore_urls
from wagtail.contrib.sitemaps.views import sitemap

from aratinga.views import robots
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

urlpatterns = [
    # Aratinga custom URLs
    path(r"robots.txt", robots, name="cms_robots"),
    path(r"sitemap.xml", sitemap, name="cms_sitemap"),
    re_path(r'^favicon\.ico$', favicon_view),
    # Wagtail
    path("", include(wagtailcore_urls)),
    # outras URLs
]
