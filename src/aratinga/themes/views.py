from django.shortcuts import render, redirect
from .models import Theme

def activate_theme(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    # Desativar todos os temas
    Theme.objects.update(active=False)
    # Ativar o tema selecionado
    theme.active = True
    theme.save()
    return redirect('home')