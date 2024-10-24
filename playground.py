import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os

page = None

def change_frame(menu):
       page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=menu).click() 

def up_file(file):
    page.wait_for_selector('//input[@type="file"]', state='attached')
    upload_field = page.locator('//input[@type="file"]').set_input_files(os.path.abspath(os.path.join("files", file)))

def search():
    search = page.locator("label").filter(has_text="Search").click()
    choose_model = page.get_by_label("Selected Fortics. **Modelos**").fill("Modelo de tes")
    choose_model = page.get_by_label("Selected Fortics. **Modelos**").press("Enter")
    ask_search = page.get_by_placeholder("Faça uma pergunta para listar").fill("GOgenier")
    ask_search = page.get_by_placeholder("Faça uma pergunta para listar").press("Enter")
    time.sleep(5)

def copilot():
    copilot = page.locator("label").filter(has_text="Copilot").click()
    # choose_model = page.get_by_label("Selected Fortics. **Modelos**").fill("Modelo de tes")
    # choose_model = page.get_by_label("Selected Fortics. **Modelos**").press("Enter")
    time.sleep(2)
    ask_copilot = page.get_by_test_id("stChatInputTextArea").fill("O que é o GOgenier?") 
    ask_copilot = page.get_by_test_id("stChatInputTextArea").press("Enter") 
    time.sleep(5)

def chat():
    chat= page.locator("label").filter(has_text="Chat").click()
    # choose_model = page.get_by_label("Selected Fortics. **Modelos**").fill("Modelo de tes")
    # choose_model = page.get_by_label("Selected Fortics. **Modelos**").press("Enter")
    time.sleep(2)
    ask_copilot = page.get_by_test_id("stChatInputTextArea").fill("O que é o GOgenier?") 
    ask_copilot = page.get_by_test_id("stChatInputTextArea").press("Enter") 
    time.sleep(5)

def insights():
    insights = page.locator("label").filter(has_text="Insights").click()
    choose_pipeline = page.get_by_label("Selected Escolha um pipeline").fill("insights")
    choose_pipeline = page.get_by_label("Selected Escolha um pipeline").press("Enter")
    time.sleep(2)
    up_file("audio.flac")
    time.sleep(15)

def stt():
    stt = page.locator("label").filter(has_text="STT").click()
    send = page.locator("label").filter(has_text="Enviar").click()
    up_file("audio.flac")
    time.sleep(10)


def talk_to_agent(agent, question):
    select_agent = page.get_by_label("Escolha um agente para").fill(agent)
    select_agent = page.get_by_label("Escolha um agente para").press("Enter")
    time.sleep(2)
    asking = page.get_by_test_id("stChatInputTextArea").fill(question)
    asking = page.get_by_test_id("stChatInputTextArea").press("Enter")
    time.sleep(15)

def talk_to_model():
    change_frame("Home")
    time.sleep(5)
    change_frame("Playground")
    search()

    # when its a tenant specifically for testing, create a loop to talk with all agents
def agents():
    agents = page.locator("label").filter(has_text="Agentes").click()


    def talk_to_db():
        talk_to_agent("Agente de cadastro database", "Sou o Pedro, me registre em seu banco de dados")
        time.sleep(5)

        message = page.get_by_test_id("stChatMessage").nth(1).text_content()
        if "Você foi registrado com sucesso" not in message:
            print("deu pau no cadastro do db")
        else:
            talk_to_agent("Agente de cadastro database", "Agora quero consultar esse banco de dados")
            print("passou no registro")

            message2 = page.get_by_test_id("stChatMessage").nth(3).text_content()
            if "registros que temos no banco de dados" not in message2:
                print("nao passou na consulta")
            else:
                print("passou em tudo")
        time.sleep(15)


    def talk_to_flow():
        talk_to_agent("Agente de teste Flow", "acione o flow e envie esta mensagem")
        time.sleep(4)

        message = page.get_by_test_id("stChatMessage").nth(1).text_content()
        if "O flow foi acionado com" not in message:
            print("deu pau na chamada do flow")
        else:
            print("deu boa")

    talk_to_agent("Agente de teste com modelo", "o que e o gogenier?")    
    # talk_to_agent("Agente de teste com dataset", "que dia é hoje e que horas sao")
    # talk_to_agent("Agente de teste CNPJ", "valide o cnpj: 54.463.890/0001-05")
    # talk_to_db()
    # talk_to_flow()



def play_ground():
    try:
        change_frame("Playground", timeout=2000)
    except Exception:
        change_frame("Home")
        change_frame("Playground")

    search()
    copilot()
    chat()
    insights()
    stt()
    agents()

def set_page(main_page):
    global page
    page = main_page 