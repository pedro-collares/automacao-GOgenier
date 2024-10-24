from playwright.sync_api import Playwright, sync_playwright, expect
import time

page = None

def login(password):
        page.get_by_label("Nome de usuário").fill("automacao")
        page.get_by_label("Senha").fill(password)
        page.get_by_test_id("stBaseButton-secondaryFormSubmit").click()
        time.sleep(2)




def set_page(main_page):
    global page
    page = main_page 