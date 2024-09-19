from django import template

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
