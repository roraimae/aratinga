from django.core.exceptions import ImproperlyConfigured
from wagtail.models import Site

from aratinga.themes.settings import ThemeSettings
from aratinga.themes.thread import set_theme


from django.conf import settings
from .models import Theme


class ThemeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        site = Site.find_for_request(request)

        if site is None:
            raise ImproperlyConfigured("Site not found!")

        theme_settings = ThemeSettings.for_site(site)
        theme = theme_settings.theme

        if theme is not None:
            try:
                active_theme = Theme.objects.get(active=True)
                settings.TEMPLATES[0]['DIRS'] = [f'themes/{active_theme.name}']
            except Theme.DoesNotExist:
                pass
            set_theme(theme)

        response = self.get_response(request)
        return response