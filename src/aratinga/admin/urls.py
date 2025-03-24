from django.urls import include
from django.urls import path
from wagtail.admin import urls as wagtailadmin_urls


urlpatterns = [
    path(
        "",
        include(wagtailadmin_urls),
    ),
]
