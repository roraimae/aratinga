# aratinga/src/aratinga/tests/endpoint_to_endpoint/test_theme_crud.py

import pytest
from playwright.sync_api import Page, expect
from django.urls import reverse
from pathlib import Path

DUMMY_THEME_PATH = Path(__file__).parent / 'aratinga-theme_test_e2e.zip'

@pytest.mark.django_db
def test_admin_pode_criar_um_novo_tema(page: Page, live_server, admin_user):
    """
    Testa o fluxo E2E de criação de um novo registro de Tema no admin.

    1. Faz login como administrador.
    2. Navega até a listagem de temas.
    3. Clica em "Add a theme".
    4. Preenche o formulário com dados válidos.
    5. Submete o formulário e verifica a mensagem de sucesso.
    6. Verifica se o novo tema aparece na listagem.
    """

    # 1. Login
    login_url = f"{live_server.url}/admin/login/"
    page.goto(login_url)
    page.fill('input[name="username"]', admin_user.username)
    page.fill('input[name="password"]', "Admin.Tester@001")
    page.click('button[type="submit"]')
    expect(page.get_by_role("button", name="Configurações")).to_be_visible()

    # 2. Navegar para a Gestão de Temas
    themes_url = f"{live_server.url}{reverse('aratingathemes:index')}"
    page.goto(themes_url)
    expect(page.get_by_text("Add a theme")).to_be_visible()

    # 3. Clicar para Adicionar Novo Tema
    page.click("a:has-text('Add a theme')")
    expect(page.get_by_text("Add theme")).to_be_visible()

    # 4. Preencher o Formulário
    theme_name = "Meu Tema E2E"
    extracted_from_path = "test_e2e"
    # 4.1. Preencher campos
    page.fill('input[name="name"]', theme_name)
    page.fill('textarea[name="description"]', "Descrição de teste E2E")
    # 4.2. Importar arquivo './aratinga-theme_test_e2e.zip' (arquivo html do mysite 'mysite/themes/bootstrap/index.html')
    page.get_by_label("Zip file*").set_input_files(DUMMY_THEME_PATH)

    # 5. Enviar o Formulário
    page.click('button:has-text("Criar")')

    # 6. Verificar o Resultado
    success_msg = f"Theme '{theme_name}' created."
    expect(page.get_by_text(success_msg)).to_be_visible()
    expect(page.get_by_role("link", name=theme_name)).to_be_visible()
    expect(page.get_by_text(extracted_from_path)).to_be_visible()