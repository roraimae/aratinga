from django import template
from aratinga import __version__
from aratinga.settings import cms_settings as cms_settings_obj
from aratinga.admin import thread

register = template.Library()


@register.filter
def get_name_of_class(class_type):
    if hasattr(class_type.__class__, "search_name"):
        return class_type.__class__.search_name
    elif hasattr(class_type.__class__, "_meta") and hasattr(
        class_type.__class__._meta, "verbose_name"
    ):
        return class_type.__class__._meta.verbose_name
    else:
        return class_type.__class__.__name__



@register.simple_tag
def aratinga_version():
    return __version__


@register.simple_tag
def django_setting(value):
    return getattr(cms_settings_obj, value)

