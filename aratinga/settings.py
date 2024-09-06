import os

from django.apps import apps
from django.conf import settings


class _DefaultSettings:
    CMS_THEME = "Bootstrap"

cms_settings = _DefaultSettings()