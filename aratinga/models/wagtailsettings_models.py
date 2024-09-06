from wagtail.contrib.settings.models import register_setting

def conditional_register_setting(condition):
    def decorator(cls):
        if condition:
            register_setting(cls)
        return cls
    return decorator



from aratinga.settings import cms_settings