# Generated by Django 5.1.7 on 2025-03-24 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aratinga', '0008_theme_themesettings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.DeleteModel(
            name='ThemeSettings',
        ),
    ]
