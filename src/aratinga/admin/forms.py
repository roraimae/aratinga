import os
import zipfile
import tempfile
import re
from django import forms
from .models import Theme
from aratinga.admin import settings


class ThemeForm(forms.ModelForm):

    zip_file = forms.FileField()
    
    class Meta:
        model = Theme
        fields = ['name', 'description','zip_file']
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['zip_file']:
            zip_file = self.cleaned_data['zip_file']
            theme_folder = re.search(r"aratinga-theme_(.*.).zip", zip_file.name)
            theme_path = os.path.join(settings.ARATINGA_THEME_PATH)

            if hasattr(zip_file, 'temporary_file_path'):
                # Se o arquivo tiver o método temporary_file_path, use-o
                temp_path = zip_file.temporary_file_path()
            else:
                # Caso contrário, salve o arquivo em um local temporário
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                for chunk in zip_file.chunks():
                    temp_file.write(chunk)
                temp_file.close()
                temp_path = temp_file.name

            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(theme_path)
            # Remover o arquivo temporário se ele foi criado
            if not hasattr(zip_file, 'temporary_file_path'):
                os.remove(temp_path)
            
            instance.theme_path = os.path.join(theme_path, theme_folder.group(1))
        if commit:
            instance.save()
        return instance
