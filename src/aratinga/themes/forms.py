import os
import zipfile
import shutil
from django import forms
from .models import Theme
from django.conf import settings


class ThemeForm(forms.ModelForm):

    zip_file = forms.FileField()
    
    class Meta:
        model = Theme
        fields = ['name', 'description', 'is_active','zip_file']
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['zip_file']:
            zip_file = self.cleaned_data['zip_file']
            theme_path = os.path.join(settings.BASE_DIR)
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(theme_path)
            os.remove(zip_file.temporary_file_path())
            instance.theme_path = theme_path
        if commit:
            instance.save()
        return instance
