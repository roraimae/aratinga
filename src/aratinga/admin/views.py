from django.shortcuts import redirect
from .models import Theme
from wagtail.admin.viewsets.model import ModelViewSet
from django.utils.translation import gettext_lazy as _

from wagtail.admin.ui.tables import Column, StatusFlagColumn, TitleColumn
from wagtail.admin.views import generic
from wagtail.permissions import site_permission_policy
from .forms import ThemeForm


class IndexView(generic.IndexView):
    page_title = _("Themes")
    add_item_label = _("Add a theme")
    context_object_name = "themes"
    default_ordering = "name"
    columns = [
        TitleColumn(
            "name",
            label=_("Theme"),
            sort_key="name",
            url_name="aratingathemes:edit",
        ),
        Column("description"),
        Column("theme_path"),
    ]


class CreateView(generic.CreateView):
    page_title = _("Add theme")
    success_message = _("Theme '%(object)s' created.")
    error_message = _("The theme could not be saved due to errors.")


class EditView(generic.EditView):
    success_message = _("Theme '%(object)s' updated.")
    error_message = _("The theme could not be saved due to errors.")
    delete_item_label = _("Delete theme")
    context_object_name = "theme"


class DeleteView(generic.DeleteView):
    success_message = _("Theme '%(object)s' deleted.")
    page_title = _("Theme site")
    confirmation_message = _("Are you sure you want to delete this theme?")


class ThemeViewSet(ModelViewSet):
    icon = "view"
    model = Theme
    permission_policy = site_permission_policy
    add_to_reference_index = False

    index_view_class = IndexView
    add_view_class = CreateView
    edit_view_class = EditView
    delete_view_class = DeleteView

    template_prefix = "aratingathemes/"

    def get_common_view_kwargs(self, **kwargs):
        return super().get_common_view_kwargs(
            **{
                "history_url_name": None,
                "usage_url_name": None,
                **kwargs,
            }
        )

    def get_form_class(self, for_update=False):
        return ThemeForm