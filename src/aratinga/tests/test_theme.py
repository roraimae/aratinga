import os
import pytest
from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
from aratinga.admin.models import Theme
from aratinga.admin.settings import ThemeSettings
from wagtail.models import Site

@pytest.mark.django_db
class ThemeAdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='adminTester', email='admintester@example.com', password='Admin.Tester@001'
        )
        self.client.login(username='adminTester', password='Admin.Tester@001')

    def test_create_theme_universitario(self):
        theme = Theme.objects.create(
            name='Tema Universitário',
            description='Tema padrão para instituições de ensino',
            theme_path='/themes/universitario'
        )
        self.assertEqual(str(theme), 'Tema Universitário')
        self.assertTrue(Theme.objects.filter(name='Tema Universitário').exists())

    def test_create_theme_govbr(self):
        theme = Theme.objects.create(
            name='Gov.br',
            description='Tema institucional do governo',
            theme_path='/themes/govBr'
        )
        self.assertEqual(theme.name, 'Gov.br')
        self.assertTrue(Theme.objects.filter(name='Gov.br').exists())

    def test_assign_theme_to_site(self):
        theme = Theme.objects.create(name='Bootstrap', theme_path='/themes/bootstrap')
        site = Site.objects.get(is_default_site=True)
        settings = ThemeSettings.for_site(site)
        settings.theme = theme
        settings.save()
        self.assertEqual(settings.theme.name, 'Bootstrap')

    def test_list_available_themes(self):
        Theme.objects.create(name='Bootstrap', theme_path='/themes/bootstrap')
        Theme.objects.create(name='Gov.br', theme_path='/themes/govBr')
        themes = Theme.objects.all()
        print("Temas no banco de dados: ", [t.name for t in themes])
        self.assertEqual(themes.count(), 3)

    def test_theme_path_exists(self):
        os.makedirs('/themes/govBr', exist_ok=True)
        theme = Theme.objects.create(name='Gov.br', theme_path='/themes/govBr')
        self.assertTrue(os.path.exists(theme.theme_path))