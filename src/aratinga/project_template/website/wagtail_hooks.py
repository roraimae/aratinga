from wagtail import hooks
from .models import WebPage

@hooks.register('after_create_page')
def set_initial_page(request, page):
    if isinstance(page, WebPage):
        # Aqui você pode definir os comportamentos adicionais desejados
        pass


@hooks.register('construct_main_menu')
def set_default_page(request, menu_items):
    if WebPage.objects.count() == 0:
        WebPage(
            title="Página Inicial",
            slug="home",
            intro="Bem-vindo à Página Inicial"
        ).save()