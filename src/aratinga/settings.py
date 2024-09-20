import os
from django.apps import apps
from django.conf import settings

class _DefaultSettings:
    CMS_THEME = "Bootstrap"
    CMS_DISABLE_LAYOUT = False
    CMS_DISABLE_NAVBAR = False
    CMS_DISABLE_FOOTER = False

    CMS_FRONTEND_NAVBAR_COLLAPSE_MODE_CHOICES = []
    CMS_FRONTEND_NAVBAR_COLOR_SCHEME_CHOICES = []
    CMS_FRONTEND_NAVBAR_FORMAT_CHOICES = []
    CMS_FRONTEND_NAVBAR_CLASS_DEFAULT = []
    CMS_FRONTEND_NAVBAR_COLLAPSE_MODE_DEFAULT = []
    CMS_FRONTEND_NAVBAR_COLOR_SCHEME_DEFAULT = []
    CMS_FRONTEND_NAVBAR_FORMAT_DEFAULT = []

    CMS_PROTECTED_MEDIA_URL = "/protected/"
    CMS_PROTECTED_MEDIA_ROOT = os.path.join(settings.BASE_DIR, "protected")
    CMS_PROTECTED_MEDIA_UPLOAD_WHITELIST = []
    CMS_PROTECTED_MEDIA_UPLOAD_BLACKLIST = [
        ".app",
        ".bat",
        ".exe",
        ".jar",
        ".php",
        ".pl",
        ".ps1",
        ".py",
        ".rb",
        ".sh",
    ]

cms_settings = _DefaultSettings()
