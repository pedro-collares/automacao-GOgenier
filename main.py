import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import data_source as d
import models as m
import agents as a
import playground as p
import integration as i


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1870, "height": 880})
    page = context.new_page()
    page.goto("https://app.genier.ai/qa/")


    for j in [d,m,a,p,i]:
        j.set_page(page)

    def login():
        page.get_by_label("Nome de usuário").fill("pedro")
        page.get_by_label("Senha").fill("@Collares123")
        page.get_by_test_id("stBaseButton-secondaryFormSubmit").click()
        time.sleep(2)
        
    login()
    # d.manage_data()
    # m.manage_model()
    # a.manage_agents()
    # p.play_ground()
    i.manage_integration()

    time.sleep(300)

    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
