from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from wagtail import hooks
from wagtail.admin.menu import MenuItem
from wagtail.permissions import site_permission_policy

from .views import ThemeViewSet


@hooks.register("register_admin_viewset")
def register_viewset():
    return ThemeViewSet("aratingathemes", url_prefix="themes")


class ThemesMenuItem(MenuItem):
    def is_shown(self, request):
        return site_permission_policy.user_has_any_permission(
            request.user, ["add", "change", "delete"]
        )


@hooks.register("register_settings_menu_item")
def register_themes_menu_item():
    return ThemesMenuItem(
        _("Themes"),
        reverse("aratingathemes:index"),
        name="themes",
        icon_name="view",
        order=602,
    )