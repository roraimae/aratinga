from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AratingaAdminAppConfig(AppConfig):
    name = "aratinga.admin"
    label = "aratingaadmin"
    verbose_name = _("Aratinga admin")
    default_auto_field = "django.db.models.AutoField"