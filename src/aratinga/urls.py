from django.urls import include
from django.urls import path
from django.urls import re_path
from wagtail import urls as wagtailcore_urls
from wagtail.contrib.sitemaps.views import sitemap

from aratinga.settings import cms_settings
from aratinga.views import robots


urlpatterns = [
    # Aratinga custom URLs
    path(r"robots.txt", robots, name="cms_robots"),
    path(r"sitemap.xml", sitemap, name="cms_sitemap"),
    # Wagtail
    path("", include(wagtailcore_urls)),
]
