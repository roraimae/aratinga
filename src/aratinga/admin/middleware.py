from django.core.exceptions import ImproperlyConfigured
from wagtail.models import Site

from .settings import ThemeSettings
from aratinga.admin.thread import set_theme


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
            theme = theme_settings.theme

            if theme is not None:
                set_theme(theme)
            
        except ThemeSettings.DoesNotExist:
            pass

        response = self.get_response(request)
        return response