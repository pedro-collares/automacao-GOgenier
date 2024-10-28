import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pytesseract
from PIL import Image
import login as l


page = None

def menu(menu):
       page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=menu).click() 

def fields(field, data):
    page.get_by_label(field).fill(data)

def resolve_captcha():
    time.sleep(1)

    captcha_element = page.get_by_role("img", name="0")
    captcha_element.screenshot(path='captcha.png')

    captcha = pytesseract.image_to_string(Image.open('captcha.png'))
    return captcha


# unfunctional because captcha is unreadable (just paying a 2captcha api key)
def new_user():
    menu("Configurações")
    # abrir o expander de usuarios
    page.locator("summary").filter(has_text="Cadastro de usuário").click()

    fields("First name", "teste")
    fields("Last name", "automacao")
    fields("Email", "pedro.collares05@gmail.com")
    fields("Nome de usuário", "automacao")
    page.get_by_label("Senha", exact=True).fill("Automac@o123")
    page.get_by_label("Repita a senha", exact=True).fill("Automac@o123")
    fields("Password hint", "automacao")
    time.sleep(5)
    
    captcha = resolve_captcha()
    fields("Captcha", captcha)


def change_llm():
    menu("Configurações")
    page.get_by_role("tab", name="Configurações avançadas").click()
    page.locator("label").filter(has_text=re.compile(r"^Gemini$")).click()
    page.get_by_role("button", name="Salvar").click()

    time.sleep(2)

    menu("Documentação")
    time.sleep(2)
    menu("Configurações")
    page.get_by_role("tab", name="Configurações avançadas").click()
    page.get_by_test_id("stRadio").locator("label").filter(has_text="OpenAI").click()
    page.get_by_role("button", name="Salvar").click()
    time.sleep(2)

def new_pass(old_pass, new_pass):
        menu("Configurações")
        page.locator("summary").filter(has_text="Troca de senha").click()
        page.get_by_label("Senha atual").fill(old_pass)
        page.get_by_label("Senha nova", exact=True).fill(new_pass)
        page.get_by_label("Repita a senha nova").fill(new_pass)
        page.get_by_role("button", name="Trocar").click()
        time.sleep(3)


def change_password():
    menu("Configurações")
    page.get_by_role("tab", name="Usuários").click()
    new_pass("Automac@o123", "Automac@o321")    

    page.get_by_test_id("stSidebarUserContent").get_by_test_id("stBaseButton-secondary").click()
    l.login("Automac@o321")
    new_pass("Automac@o321", "Automac@o123")


def set_page(main_page):
    global page
    page = main_page 