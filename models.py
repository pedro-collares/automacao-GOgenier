import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

page = None



def select_model():
    page.get_by_label("Escolha um modelo").fill("Modelo de teste")
    page.get_by_label("Escolha um modelo").press("Enter")

def menu(menu):
       page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=menu).click() 

def manage_model():
    page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=" Modelos").click()
    
    def create_model():
        time.sleep(1)
        page.get_by_label("Nome do modelo").fill("Modelo de teste")
        page.get_by_test_id("stMultiSelect").get_by_role("img", name="open").click()
        page.get_by_role("option", name="fonte de testes").click()
        page.get_by_test_id("stBaseButton-secondaryFormSubmit").click()

        def process():
            time.sleep(5)
            select_model()
            page.get_by_role("button", name="rule_settings icon Processar/").click()
            time.sleep(15)

        process()

    def delete_model():
        while(True):
            try:
                select_model()
                page.get_by_role("button", name="delete icon Excluir").click()
                page.get_by_role("button", name="warning icon Confirmar").click()
                time.sleep(1)
            except Exception:
                break


    def modify_model():
        select_model()
        num_od_docs = page.get_by_test_id("stNumberInputStepUp").click()
        page.get_by_role("button", name="save icon Salvar").click()

        

    create_model()
    # modify_model()
    # delete_model()

def reprocess():
    page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=" Modelos").click()
    select_model()
    page.get_by_role("button", name="reset_settings icon").click()
    time.sleep(90)
    print("reprocessado")
    menu("Modelos")


def set_page(main_page):
    global page
    page = main_page    