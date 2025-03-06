from django.db import migrations


def initial_data(apps, schema_editor):
    Theme = apps.get_model('aratingathemes', 'Theme')
    # Create a new default site

class Migration(migrations.Migration):

    dependencies = [
        ('aratingathemes', '0001_initial'),
        ('aratingathemes', '0002_themesettings'),
        ('aratingathemes', '0003_themesettings_theme_alter_themesettings_id'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]



