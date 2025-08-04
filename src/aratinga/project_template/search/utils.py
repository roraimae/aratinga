from django.apps import apps
from wagtail.models import Page

def get_all_page_classes():
    all_models = apps.get_models()
    page_classes = [model for model in all_models if issubclass(model, Page)]
    return page_classes