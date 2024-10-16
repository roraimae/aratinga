from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AratingaAdminAppConfig(AppConfig):
    name = "aratinga.admin_themes"
    label = "aratingathemes"
    verbose_name = _("Aratinga Themes")
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        from wagtail.admin.signal_handlers import register_signal_handlers

        register_signal_handlers()