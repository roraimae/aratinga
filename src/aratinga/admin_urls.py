from django.urls import include
from django.urls import path
from wagtail.admin import urls as wagtailadmin_urls

from aratinga.views import import_index
from aratinga.views import import_pages_from_csv_file


urlpatterns = [
    path(
        "aratinga/import-export/",
        import_index,
        name="import_index",
    ),
    path(
        "aratinga/import-export/import_from_csv/",
        import_pages_from_csv_file,
        name="import_from_csv",
    ),
    path(
        "",
        include(wagtailadmin_urls),
    ),
]
