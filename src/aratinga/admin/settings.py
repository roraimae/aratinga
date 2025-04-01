from wagtail.admin.panels import Panel
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from wagtail import VERSION as WAGTAIL_VERSION
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import register_setting
from django.core.files.storage import FileSystemStorage
from .models import Theme

if WAGTAIL_VERSION < (4, 0):
    from wagtail.contrib.settings.models import BaseSetting
else:
    from wagtail.contrib.settings.models import BaseSiteSetting as BaseSetting

__ALL__ = ["ThemeSettings"]

theme_storage = FileSystemStorage(settings.BASE_DIR)

## Aratinga themes
ARATINGA_THEME_PATH = 'themes'

class ThemeManagementPanel(Panel):
    def render(self):
        # Render a custom template that includes both activation and installation forms
        return render(self.request, 'aratinga/theme_management.html', {
            'themes': Theme.objects.all(),  # List of available themes
            'current_theme': self.instance.theme,  # Currently active theme
        })

    def on_form_submit(self, request):
        # Handle form submission for both activation and installation
        if 'activate_theme' in request.POST:
            theme_id = request.POST.get('theme_id')
            self.instance.theme_id = theme_id
            self.instance.save()
        elif 'install_theme' in request.POST:
            # Logic to handle theme installation
            pass
        return HttpResponseRedirect(reverse('wagtailadmin_home'))

@register_setting
class ThemeSettings(BaseSetting):
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )

    theme = models.ForeignKey( Theme,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Themes"),)

    panels = [FieldPanel("theme")]

    class Meta:
        verbose_name = _("themes")
        verbose_name_plural = _("themes")
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)