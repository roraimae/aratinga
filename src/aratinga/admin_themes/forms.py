import os
import zipfile

from django import forms
from .models import Theme
from django.conf import settings


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'description', 'active','zip_file']
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['zip_file']:
            with zipfile.ZipFile(self.cleaned_data['zip_file'], 'r') as zip_ref:
                extract_path = settings.BASE_DIR
                zip_ref.extractall(extract_path)
            # Apague o arquivo zip após descompactar
            os.remove(self.cleaned_data['zip_file'].path)
        if commit:
            instance.save()
        return instance
