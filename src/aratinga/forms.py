"""
Enhancements to wagtail.contrib.forms.
"""

from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType


class SearchForm(forms.Form):
    s = forms.CharField(
        max_length=255,
        required=False,
        label=_("Search"),
    )
    t = forms.CharField(
        widget=forms.HiddenInput,
        max_length=255,
        required=False,
        label=_("Page type"),
    )

def get_page_model_choices():
    """
    Returns a list of tuples of all creatable Arainga pages
    in the format of (app_label:model, "Verbose Name")
    """
    from aratinga.models import get_page_models

    rval = []
    for page in get_page_models():
        if page.is_creatable:
            ct = ContentType.objects.get_for_model(page)
            rval.append((f"{ct.app_label}:{ct.model}", ct.name))
    return rval
