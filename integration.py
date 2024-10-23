import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

page = None

def change_frame(menu):
    page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=menu).click()   

def create():
    page.frame_locator("iframe").nth(3).get_by_title("Crear novo").click()
    time.sleep(5)
    
    page.frame_locator("iframe").nth(3).locator("ui-component").filter(has_text="Nome:").locator("div").nth(1).fill("Integração teste de automação")
    time.sleep(20)
    page.locator("iframe").nth(3).content_frame().locator("ui-component").filter(has_text="Nome:").get_by_role("textbox")
    page.locator("iframe").nth(3).content_frame().locator("ui-component").filter(has_text="Proxy endpoint:/fluxoN/").get_by_role("textbox").fill("/automacao/")
    page.locator("iframe").nth(3).content_frame().get_by_role("button", name=" ENVIAR").click()






def manage_integration():
    change_frame("Integração")
    time.sleep(10)
    create()

def set_page(main_page):
    global page
    page = main_page 