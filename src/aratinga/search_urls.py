from django.urls import path

from aratinga.views import search


urlpatterns = [
    path("", search, name="aratinga_search"),
]
