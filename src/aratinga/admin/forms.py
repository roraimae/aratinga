import os
import re
import zipfile
import tempfile

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Theme
from aratinga.admin import settings


class ThemeForm(forms.ModelForm):

    zip_file = forms.FileField(
        label=_("Theme ZIP file"),
        help_text=_("Upload a ZIP file named aratinga-theme_<name>.zip"),
    )

    class Meta:
        model = Theme
        fields = ["name", "description", "zip_file"]

    def clean_zip_file(self):
        zip_file = self.cleaned_data["zip_file"]
        if not re.search(r"^aratinga-theme_(.+)\.zip$", zip_file.name):
            raise ValidationError(
                _(
                    "The ZIP file must be named aratinga-theme_<name>.zip "
                    "(e.g. aratinga-theme_bootstrap.zip)."
                )
            )
        return zip_file

    def save(self, commit=True):
        instance = super().save(commit=False)
        zip_file = self.cleaned_data["zip_file"]

        theme_name_match = re.search(r"^aratinga-theme_(.+)\.zip$", zip_file.name)
        theme_name = theme_name_match.group(1)
        theme_path = settings.ARATINGA_THEME_PATH

        if hasattr(zip_file, "temporary_file_path"):
            temp_path = zip_file.temporary_file_path()
            own_temp = False
        else:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
            for chunk in zip_file.chunks():
                temp_file.write(chunk)
            temp_file.close()
            temp_path = temp_file.name
            own_temp = True

        try:
            with zipfile.ZipFile(temp_path, "r") as zip_ref:
                # Sanitize against zip slip: reject any entry whose resolved
                # path escapes the target directory.
                abs_theme_path = os.path.realpath(theme_path)
                for member in zip_ref.namelist():
                    member_path = os.path.realpath(
                        os.path.join(abs_theme_path, member)
                    )
                    if not member_path.startswith(abs_theme_path + os.sep):
                        raise ValidationError(
                            _("The ZIP file contains unsafe paths and cannot be extracted.")
                        )
                zip_ref.extractall(abs_theme_path)
        finally:
            if own_temp:
                os.remove(temp_path)

        instance.theme_path = os.path.join(theme_path, theme_name)
        if commit:
            instance.save()
        return instance
