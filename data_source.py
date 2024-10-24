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
    time.sleep(5)

def save_data():
    page.get_by_role("button", name="save icon Salvar").click() 
    time.sleep(3)

    
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
        try:
            page.get_by_role("combobox", name="Selected Conteúdos da WEB").fill("conteúdo de vídeo")
            page.get_by_role("combobox", name="Selected Conteúdos da WEB").press("Enter")
        except Exception:
            type_of_data("conteúdo de vídeo")

        page.get_by_label("Endereço do video (um endereç").fill("https://www.youtube.com/watch?v=Ss_S0n53Ysc&t=4408s&pp=ygUIZ29nZW5pZXI%3D")
        save_data()

    def input_pdf():
        try:
            page.get_by_role("combobox", name="Selected Conteúdo de vídeos do Youtube").fill("Arquivos de texto e") 
            page.get_by_role("combobox", name="Selected Conteúdo de vídeos do Youtube").press("Enter") 
        except Exception:
            type_of_data("Arquivos de texto e")
     
        up_file("GOgenier.pdf")
        
    
    def input_audio():
        try:
            page.get_by_role("combobox", name="Selected Arquivos de texto").fill("Áudios e vídeos") 
            page.get_by_role("combobox", name="Selected Arquivos de texto").press("Enter") 
            time.sleep(2)
        except Exception:
            type_of_data("Áudios e vídeos")
        up_file("audio.flac")


    def input_text():
        try:
            page.get_by_role("combobox", name="Selected Áudios e vídeos").fill("Edite um texto na") 
            page.get_by_role("combobox", name="Selected Áudios e vídeos").press("Enter") 
            time.sleep(2)
        except Exception:
            type_of_data("Edite um texto na")
        page.get_by_label("Conteúdo").fill("Este é um texto de teste para a automação dos testes do GOgenier")
        time.sleep(3)
        page.get_by_role("button", name="Salvar").click()
        time.sleep(2)

    def input_csv():
        try:
            page.get_by_role("combobox", name="Selected Edite um texto na hora").fill("Arquivos estruturados") 
            page.get_by_role("combobox", name="Selected Edite um texto na hora").press("Enter") 
            time.sleep(2)
        except Exception:
            type_of_data("Arquivos estruturados")
        up_file("produtos_ficticios_corrigido.csv")
        save_data()

    input_webdata()
    input_youtube()
    input_pdf()
    input_audio()
    input_text()
    input_csv()


        
def remove_data():
    page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=" Fontes de dados").click()
    page.get_by_text("fonte de testes").click()

    type_of_data("Conteúdos da ")
    page.get_by_label("Endereço WEB (um endereço por").clear()
    save_data()
    time.sleep(5)

    page.get_by_role("combobox", name="Selected Conteúdos da WEB").fill("Conteúdo de vídeo")
    page.get_by_role("combobox", name="Selected Conteúdos da WEB").press("Enter")
    
    page.get_by_label("Endereço do video (um endereço por linha),").clear()
    save_data()

    time.sleep(2)


    # clear_cache_ds()



def set_page(main_page):
    global page
    page = main_page    