from django.db import migrations


def initial_data(apps, schema_editor):
    Theme = apps.get_model('aratingathemes', 'Theme')
    # Create a new default site
    Theme.objects.get_or_create(
        id=1,
        defaults={
            name='bootstrap5',
            description='Bootstrap 5' ,
            theme_path='themes/bootstrap5',
            is_active=True
        },
    )
    
        # Create a new default site
    Theme.objects.get_or_create(
        id=2,
        defaults={
            name='tailwind',
            description='Tailwind' ,
            theme_path='themes/tailwind',
            is_active=False
        }
    )

class Migration(migrations.Migration):

    dependencies = [
        ('aratingathemes', '0001_initial'),
        ('aratingathemes', '0002_themesettings'),
        ('aratingathemes', '0003_themesettings_theme_alter_themesettings_id'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]



