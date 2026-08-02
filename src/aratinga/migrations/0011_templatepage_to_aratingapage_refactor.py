"""
Refactors TemplatePage to inherit from AratingaPage instead of Page directly.
Also renames the `template` FK to `snippet_template` to avoid shadowing
Wagtail's Page.template string attribute.

Steps:
  1. Add aratingapage_ptr as a nullable OneToOneField temporarily.
  2. Data migration: for each existing TemplatePage, ensure a corresponding
     AratingaPage row exists and wire aratingapage_ptr to it.
  3. Make aratingapage_ptr non-nullable and the primary key.
  4. Drop the old page_ptr field.
  5. Rename template -> snippet_template.
"""

import django.db.models.deletion
from django.db import migrations, models


def populate_aratingapage_ptr(apps, schema_editor):
    """
    For every existing TemplatePage row, create the corresponding AratingaPage
    row (if one does not yet exist) and set aratingapage_ptr_id.

    Because AratingaPage.page_ptr_id == wagtailcore_page.id, and TemplatePage
    currently stores the same id in page_ptr_id, we can reuse that value.
    """
    AratingaPage = apps.get_model("aratinga", "AratingaPage")
    TemplatePage = apps.get_model("aratinga", "TemplatePage")

    for tp in TemplatePage.objects.all():
        page_id = tp.page_ptr_id
        # Create the AratingaPage intermediary row if it doesn't exist yet.
        aratinga_page, _ = AratingaPage.objects.get_or_create(
            page_ptr_id=page_id,
            defaults={"index_order_by": "", "custom_template": ""},
        )
        tp.aratingapage_ptr_id = aratinga_page.page_ptr_id
        tp.save(update_fields=["aratingapage_ptr_id"])


def reverse_populate_aratingapage_ptr(apps, schema_editor):
    """Restore page_ptr_id from aratingapage_ptr_id (same value)."""
    TemplatePage = apps.get_model("aratinga", "TemplatePage")
    for tp in TemplatePage.objects.all():
        tp.page_ptr_id = tp.aratingapage_ptr_id
        tp.save(update_fields=["page_ptr_id"])


class Migration(migrations.Migration):

    dependencies = [
        ("aratinga", "0010_alter_genericsettings_title_suffix"),
        ("wagtailcore", "0094_alter_page_locale"),
    ]

    operations = [
        # ── Step 1: add aratingapage_ptr as nullable so existing rows are valid ──
        migrations.AddField(
            model_name="templatepage",
            name="aratingapage_ptr",
            field=models.OneToOneField(
                auto_created=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                to="aratinga.aratingapage",
            ),
        ),
        # ── Step 2: fill aratingapage_ptr for all existing rows ──
        migrations.RunPython(
            populate_aratingapage_ptr,
            reverse_code=reverse_populate_aratingapage_ptr,
        ),
        # ── Step 3: drop the old page_ptr field ──
        # Must happen BEFORE promoting aratingapage_ptr to primary key below:
        # Postgres enforces "one primary key per table" at DDL time (unlike
        # SQLite, which rebuilds the table from the final model state and
        # never has two PK constraints coexist mid-migration), so adding a
        # second primary key while page_ptr is still one fails with
        # "multiple primary keys ... are not allowed".
        migrations.RemoveField(
            model_name="templatepage",
            name="page_ptr",
        ),
        # ── Step 4: make aratingapage_ptr the real primary key (non-nullable) ──
        migrations.AlterField(
            model_name="templatepage",
            name="aratingapage_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="aratinga.aratingapage",
            ),
        ),
        # ── Step 5: rename template -> snippet_template ──
        migrations.RenameField(
            model_name="templatepage",
            old_name="template",
            new_name="snippet_template",
        ),
        # ── Step 6: add FooterText model ──
        migrations.CreateModel(
            name="FooterText",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "body",
                    models.JSONField(blank=True, default=list, verbose_name="Body"),
                ),
                (
                    "live",
                    models.BooleanField(
                        default=True,
                        help_text="Only one footer text should be live at a time.",
                        verbose_name="Live",
                    ),
                ),
            ],
            options={
                "verbose_name": "Footer Text",
                "verbose_name_plural": "Footer Texts",
            },
        ),
    ]
