from django.apps import AppConfig


class AratingaConfig(AppConfig):
    name = "aratinga"
    verbose_name = "Aratinga CMS"
    # TODO: At some point in the future, change this to BigAutoField and create
    # the corresponding migration for concrete models in aratinga.
    default_auto_field = "django.db.models.AutoField"
