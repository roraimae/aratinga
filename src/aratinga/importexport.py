from django import forms
from wagtail.models import Page
from wagtail.admin.widgets import AdminPageChooser

from django.utils.translation import gettext as _
from aratinga.forms import get_page_model_choices

class ImportPagesFromCSVFileForm(forms.Form):
    """
    Mostly copied from:
    https://github.com/torchbox/wagtail-import-export/blob/master/wagtailimportexport/forms.py#L29
    with addition of ``page_type``.
    """

    page_type = forms.ChoiceField(choices=get_page_model_choices)

    file = forms.FileField(label=_("File to import"))

    parent_page = forms.ModelChoiceField(
        queryset=Page.objects.all(),
        widget=AdminPageChooser(can_choose_root=True, show_edit_link=False),
        label=_("Destination parent page"),
        help_text=_("Imported pages will be created as children of this page."),
    )
