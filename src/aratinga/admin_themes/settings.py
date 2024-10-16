from django import forms
from django.apps import apps
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from wagtail import VERSION as WAGTAIL_VERSION
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import register_setting
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import ThemeForm

if WAGTAIL_VERSION < (4, 0):
    from wagtail.contrib.settings.models import BaseSetting
else:
    from wagtail.contrib.settings.models import BaseSiteSetting as BaseSetting

__ALL__ = ["ThemeSettings"]

theme_storage = FileSystemStorage(settings.BASE_DIR)

@register_setting(icon='folder-open-inverse')
class ThemeSettings(BaseSetting):
    name = models.CharField(max_length=100)
    description = models.TextField()
    zip_file = models.FileField(upload_to='themes/', storage=theme_storage)
    active = models.BooleanField(default=False)

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('zip_file'),
        FieldPanel('active'),
    ]

    class Meta:
        verbose_name = _("themes")
        verbose_name_plural = _("themes")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

