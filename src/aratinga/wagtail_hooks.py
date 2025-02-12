from django.utils.html import format_html
from django.templatetags.static import static
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('wagtail/theme.css'))


@hooks.register('register_snippet_menu_item')
def preview_template_menu():
    template_preview_url = reverse('preview_template', args=[1])  # Example static preview
    return MenuItem("Preview Templates", template_preview_url, classnames='icon icon-view')