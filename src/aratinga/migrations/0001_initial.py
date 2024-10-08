# Generated by Django 5.1.1 on 2024-09-20 15:28

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AratingaPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('index_order_by', models.CharField(blank=True, choices=[('', 'Default Ordering'), ('-first_published_at', 'Date first published, newest to oldest'), ('first_published_at', 'Date first published, oldest to newest'), ('-last_published_at', 'Date updated, newest to oldest'), ('last_published_at', 'Date updated, oldest to newest'), ('title', 'Title, alphabetical'), ('-title', 'Title, reverse alphabetical')], default='', help_text='Child pages will then be sorted by this attribute.', max_length=255, verbose_name='Order child pages by')),
                ('custom_template', models.CharField(blank=True, max_length=255, verbose_name='Template')),
            ],
            options={
                'verbose_name': 'Aratinga Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AratingaTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='aratinga.aratingapage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
            options={
                'verbose_name': 'CodeRed Tag',
            },
        ),
        migrations.CreateModel(
            name='LayoutSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navbar_color_scheme', models.CharField(blank=True, default='', help_text='Optimizes text and other navbar elements for use with light or dark backgrounds.', max_length=50, verbose_name='Navbar color scheme')),
                ('navbar_class', models.CharField(blank=True, default='', help_text='Custom classes applied to navbar e.g. "bg-light", "bg-dark", "bg-primary".', max_length=255, verbose_name='Navbar CSS class')),
                ('navbar_fixed', models.BooleanField(default=False, help_text='Fixed navbar will remain at the top of the page when scrolling.', verbose_name='Fixed navbar')),
                ('navbar_content_fluid', models.BooleanField(default=False, help_text='Content within the navbar will fill edge to edge.', verbose_name='Full width navbar contents')),
                ('navbar_collapse_mode', models.CharField(blank=True, default='', help_text='Control on what screen sizes to show and collapse the navbar menu links.', max_length=50, verbose_name='Collapse navbar menu')),
                ('navbar_format', models.CharField(blank=True, default='', max_length=50, verbose_name='Navbar format')),
                ('navbar_search', models.BooleanField(default=True, help_text='Show search box in navbar', verbose_name='Search box')),
                ('from_email_address', models.CharField(blank=True, help_text='The default email address this site appears to send from. For example: "sender@example.com" or "Sender Name <sender@example.com>" (without quotes)', max_length=255, verbose_name='From email address')),
                ('search_num_results', models.PositiveIntegerField(default=10, verbose_name='Number of results per page')),
                ('external_new_tab', models.BooleanField(default=False, verbose_name='Open all external links in new tab')),
                ('google_maps_api_key', models.CharField(blank=True, help_text='The API Key used for Google Maps.', max_length=255, verbose_name='Google Maps API Key')),
                ('mailchimp_api_key', models.CharField(blank=True, help_text='The API Key used for Mailchimp.', max_length=255, verbose_name='Mailchimp API Key')),
                ('favicon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favicon', to='wagtailimages.image', verbose_name='Favicon')),
                ('logo', models.ForeignKey(blank=True, help_text='Brand logo used in the navbar and throughout the site', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'CMS Settings',
            },
        ),
    ]
