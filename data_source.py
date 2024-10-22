import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os

page = None

def change_frame(menu):
    time.sleep(5)
    page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=menu).click()   

def type_of_data(type):
    page.get_by_role("combobox", name="Selected Opções de fonte de").fill(type)
    press_enter()
    
def press_enter():
    page.get_by_role("combobox", name="Selected Opções de fonte de").press("Enter")

def up_file(file):
    page.wait_for_selector('//input[@type="file"]', state='attached')
    upload_field = page.locator('//input[@type="file"]').set_input_files(os.path.abspath(os.path.join("files", file)))

def save_data():
    page.get_by_role("button", name="save icon Salvar").click() 
    
def clear_cache_ds():
    change_frame("Fontes de dados")
    page.get_by_text("fonte de testes").click()
    page.get_by_role("button", name="folder_delete icon Limpar o").click()



def manage_data():
    page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=" Fontes de dados").click()
    page.get_by_text("fonte de testes").click()

    def input_webdata():
        type_of_data("Conteúdos da ")

        page.get_by_label("Endereço WEB (um endereço por").fill("https://gogenier.ai/\nhttps://www.fortics.com.br/\nhttps://www.fortics.com.br/fortics-szchat/\nhttps://www.fortics.com.br/fortics-pbx/")
        save_data()

    def input_youtube():
        type_of_data("conteúdo de vídeo")
        page.get_by_label("Endereço do video (um endereç").fill("https://www.youtube.com/watch?v=Ss_S0n53Ysc&t=4408s&pp=ygUIZ29nZW5pZXI%3D")
        save_data()

    def input_pdf():
        type_of_data("Arquivos de texto e")
        up_file("GOgenier.pdf")
        time.sleep(5)
    
    def input_audio():
        type_of_data("Áudios e vídeos")
        up_file("audio.flac")
        time.sleep(5)
        save_data()

    def input_text():
        type_of_data("Edite um texto na")
        page.get_by_label("Conteúdo").fill("Este é um texto de teste para a automação dos testes do GOgenier")
        page.get_by_role("button", name="Salvar").click()

    def input_csv():
        type_of_data("Arquivos estruturados")
        up_file("produtos_ficticios_corrigido.csv")
        time.sleep(5)
        save_data()


    # input_webdata()
    # input_youtube()
    # input_pdf()
    # input_audio()
    # input_text()
    # input_csv()
    
    # clear_cache_ds()



def set_page(main_page):
    global page
    page = main_page    