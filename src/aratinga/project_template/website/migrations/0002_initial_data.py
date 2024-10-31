from django.db import migrations
from wagtail.models import Locale


def initial_data(apps, schema_editor):
    ContentType = apps.get_model('contenttypes.ContentType')
    Site = apps.get_model('wagtailcore.Site')
    WebPage = apps.get_model('website.WebPage')

    # Create page content type
    webpage_content_type, created = ContentType.objects.get_or_create(
        model='webpage',
        app_label='website',
    )

    homepage = WebPage.objects.create(
        title = "Home",
        slug='home',
        custom_template='aratinga/pages/web_page.html',
        content_type=webpage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
        locale_id=Locale.get_default().id,
    )

    # Create a new default site
    Site.objects.create(
        hostname='localhost',
        site_name='localhost',
        root_page_id=homepage.id,
        is_default_site=True
    )


class Migration(migrations.Migration):

    dependencies = [
        ('aratinga', '0001_initial'),
        ('wagtailcore', '0057_page_locale_fields_notnull'),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]



