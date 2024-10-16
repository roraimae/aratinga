from django.contrib import admin
from .models import Theme
from .forms import ThemeForm

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    form = ThemeForm

