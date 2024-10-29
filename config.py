import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import login as l


page = None

def menu(menu):
       page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=menu).click() 

def logout():
    page.get_by_test_id("stSidebarUserContent").get_by_test_id("stBaseButton-secondary").click()

# Funcao que altera o LLm nas configuracoes, e volta para o original
def change_llm():
    # Altera pra Gemini
    menu("Configurações")
    page.get_by_role("tab", name="Configurações avançadas").click()
    page.locator("label").filter(has_text=re.compile(r"^Gemini$")).click()
    page.get_by_role("button", name="Salvar").click()
    time.sleep(2)
    menu("Documentação")
    time.sleep(2)
    # Retorna para OpenAI
    menu("Configurações")
    page.get_by_role("tab", name="Configurações avançadas").click()
    page.get_by_test_id("stRadio").locator("label").filter(has_text="OpenAI").click()
    page.get_by_role("button", name="Salvar").click()
    time.sleep(2)

# Funcao que altera a senha do do usuario, usada na funcao a baixo
def new_pass(old_pass, new_pass):
        menu("Configurações")
        page.locator("summary").filter(has_text="Troca de senha").click()
        page.get_by_label("Senha atual").fill(old_pass)
        page.get_by_label("Senha nova", exact=True).fill(new_pass)
        page.get_by_label("Repita a senha nova").fill(new_pass)
        page.get_by_role("button", name="Trocar").click()
        time.sleep(3)

# Funcao que altera para nova senha, e troca novamente a senha do usuario
def change_password():
    # Altera a senha e da um logout
    menu("Configurações")
    page.get_by_role("tab", name="Usuários").click()
    new_pass("Automac@o123", "Automac@o321")    
    logout()

    # Loga novamente e troca para a senha original
    l.login("Automac@o321")
    new_pass("Automac@o321", "Automac@o123")


def set_page(main_page):
    global page
    page = main_page 