from django.conf import settings
from django.utils.translation import gettext as _
from wagtail import VERSION as WAGTAIL_VERSION
from wagtail.contrib.settings.models import register_setting
from django.core.files.storage import FileSystemStorage
from .models import Theme

if WAGTAIL_VERSION < (4, 0):
    from wagtail.contrib.settings.models import BaseSetting
else:
    from wagtail.contrib.settings.models import BaseSiteSetting as BaseSetting

__ALL__ = ["ThemeSettings"]

theme_storage = FileSystemStorage(settings.BASE_DIR)

@register_setting(icon='view')
class ThemeSettings(BaseSetting):
    
    themes = Theme

    class Meta:
        verbose_name = _("themes")
        verbose_name_plural = _("themes")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def list_themes(self):
        return Theme.objects.all()
