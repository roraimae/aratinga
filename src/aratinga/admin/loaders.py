import os

from aratinga.admin import settings
from django.template.loaders.filesystem import Loader as BaseLoader

from .thread import get_theme


class ThemeLoader(BaseLoader):
    """
    Theme template Loader class for serving optional themes per Aratinga site.
    """
    def get_dirs(self):
        dirs = super(ThemeLoader, self).get_dirs()
        theme = get_theme()
        theme_path = getattr(settings, 'ARATINGA_THEME_PATH', None)
        
        if theme:
            if theme_path:
                # Prepend theme path if ARATINGA_THEME_PATH is set
                theme_dirs = [os.path.join(theme.theme_path) for dir in dirs]
            else:
                # Append theme for each directory in the DIRS option of the
                # TEMPLATES setting
                theme_dirs = [os.path.join(dir, theme.theme_path) for dir in dirs]
            return theme_dirs
        
        return dirs