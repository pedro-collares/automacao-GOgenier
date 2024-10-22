import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import data_source as d
import models as m
import agents as a



def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1870, "height": 880})
    page = context.new_page()
    page.goto("https://app.genier.ai/qa/")


    for i in [d,m,a]:
        i.set_page(page)

         

    # logar
    def login():
        page.get_by_label("Nome de usuário").fill("pedro")
        page.get_by_label("Senha").fill("@Collares123")
        page.get_by_test_id("stBaseButton-secondaryFormSubmit").click()
        
    

    

    login()
    time.sleep(2)
    # d.manage_data()
    # m.manage_model()
    a.manage_agents()
    time.sleep(30)






    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
