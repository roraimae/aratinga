"""
Enhancements to wagtail.contrib.forms.
"""

from django import forms

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
