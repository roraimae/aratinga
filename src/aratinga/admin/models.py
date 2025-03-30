from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

theme_storage = FileSystemStorage(settings.BASE_DIR)

class Theme(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    theme_path = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name