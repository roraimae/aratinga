from django.core.exceptions import ImproperlyConfigured
from wagtail.models import Site

from .settings import ThemeSettings


from django.conf import settings


class ThemeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        site = Site.find_for_request(request)

        if site is None:
            raise ImproperlyConfigured("Site not found!")

        # Obter o tema ativo para o site
        try:
            theme_settings = ThemeSettings.for_site(site)
            if theme_settings.is_active:
                active_theme = theme_settings
                settings.TEMPLATES[0]['DIRS'] = [f'themes/{active_theme.name}']
        except ThemeSettings.DoesNotExist:
            pass

        response = self.get_response(request)
        return response