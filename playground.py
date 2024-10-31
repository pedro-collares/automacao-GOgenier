import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os

page = None

# Função para navegar no menu lateral, clicando em um item específico
def menu(menu):
       page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=menu).click() 

# Função que upa um arquivo (normalmente mp4, para stt e insights)
def up_file(file):
    page.wait_for_selector('//input[@type="file"]', state='attached')
    upload_field = page.locator('//input[@type="file"]').set_input_files(os.path.abspath(os.path.join("files", file)))

# Seleciona e consulta com o Search
def search():
    search = page.locator("label").filter(has_text="Search").click()
    choose_model = page.get_by_label("Selected Fortics. **Modelos**").fill("Modelo de tes")
    choose_model = page.get_by_label("Selected Fortics. **Modelos**").press("Enter")
    ask_search = page.get_by_placeholder("Faça uma pergunta para listar").fill("GOgenier")
    ask_search = page.get_by_placeholder("Faça uma pergunta para listar").press("Enter")
    time.sleep(10)

# Funcão especifica para testar o search apos reprocessamento do modelo
def talk_to_model():
    menu("Home")
    time.sleep(5)
    menu("Playground")
    search()

# Seleciona e conversa com o Copilot
def copilot():
    copilot = page.locator("label").filter(has_text="Copilot").click()
    time.sleep(2)
    ask_copilot = page.get_by_test_id("stChatInputTextArea").fill("O que é o GOgenier?") 
    ask_copilot = page.get_by_test_id("stChatInputTextArea").press("Enter") 
    time.sleep(10)

# Seleciona e conversa com o Chat
def chat():
    chat= page.locator("label").filter(has_text="Chat").click()
    time.sleep(2)
    ask_copilot = page.get_by_test_id("stChatInputTextArea").fill("O que é o GOgenier?") 
    ask_copilot = page.get_by_test_id("stChatInputTextArea").press("Enter") 
    time.sleep(20)

# Seleciona e envia o audio para o Insights
def insights():
    insights = page.locator("label").filter(has_text="Insights").click()
    choose_pipeline = page.get_by_label("Selected Escolha um pipeline").fill("Insights")
    choose_pipeline = page.get_by_label("Selected Escolha um pipeline").press("Enter")
    time.sleep(2)
    up_file("audio.flac")
    time.sleep(30)

# Seleciona e envia o audio para o STT
def stt():
    stt = page.locator("label").filter(has_text="STT").click()
    send = page.locator("label").filter(has_text="Enviar").click()
    up_file("audio.flac")
    time.sleep(15)


# Função que seleciona o agente passado no parametro, e envia a pergunta passada
def talk_to_agent(agent, question):
    time.sleep(2)
    select_agent = page.get_by_label("Escolha um agente para").fill(agent)
    select_agent = page.get_by_label("Escolha um agente para").press("Enter")
    time.sleep(2)
    asking = page.get_by_test_id("stChatInputTextArea").fill(question)
    asking = page.get_by_test_id("stChatInputTextArea").press("Enter")
    time.sleep(10)




# Funcao que seleciona agentes, e chama as funcoes talk_to...
def agents():
    agents = page.locator("label").filter(has_text="Agentes").click()

    # FUnção que seleciona um agente de database, envia a solicitacao para registrar-se no db e valida o retorno do agente
    def talk_to_db(agent):
        talk_to_agent(agent, "Sou o Pedro, me registre em seu banco de dados")

        # Validação do retorno do agente, se deu certo ou não
        message = page.get_by_test_id("stChatMessage").nth(1).text_content()
        if "foi registrado com sucesso" not in message:
            print("deu pau no cadastro do db")
        else:
            print("passou no registro")
            talk_to_agent(agent, "Agora quero consultar esse banco de dados")
            

    # Funcao que fala com o agente de flow e valida se o flow foi chamado
    def talk_to_flow(agent):
        talk_to_agent(agent, "Acione o flow e envie esta mensagem: 'Teste do Flow na automação do GOgenier' ")

        # Validação da mensagem do flow
        message = page.get_by_test_id("stChatMessage").nth(1).text_content()
        if "O flow foi acionado com" not in message:
            print("deu pau na chamada do flow")
        else:
            print("Flow esta funcionando")
    
    # Funcao que fala com o agente de flow + database + modelo e valida se as devidas acoes estao sendo realizadas
    def talk_agent_with_flow_db_model():
        # Fala com o Flow e faz a validação
        talk_to_agent("Agente com flow + db + modelo", "Acione o flow e envie esta mensagem: 'Teste do Flow + DB + modelo na automação do GOgenier' ")
        # Solicita o registro no database e faz a validação
        talk_to_agent("Agente com flow + db + modelo", "Sou o Pedro, me registre em seu banco de dados")

        message = page.get_by_test_id("stChatMessage").nth(3).text_content()
        if "foi registrado com sucesso" not in message:
            print("deu pau no cadastro do db")
        else:
            print("Cadastro do db esta funcionando")
        # Fala com o Modelo
        talk_to_agent("Agente com flow + db + modelo ", "o que é o gogenier?")
       

    # Chamada das funções que falam com os agentes
    talk_to_agent("Agente de teste com dataset", "que dia é hoje e que horas sao")
    talk_to_agent("Agente de teste CNPJ", "valide o cnpj: 54.463.890/0001-05")
    talk_agent_with_flow_db_model()
    
    #  Sugestões de conversas com outros agentes:
    talk_to_agent("Agente de teste com modelo", "o que e o gogenier?")    
    # talk_to_db("Agente de cadastro database")
    # talk_to_flow("Agente de teste Flow")


# Funcao que comanda o playground e chama o que sera testado no playground
def play_ground():
    try:
        menu("Playground", timeout=2000)
    except Exception:
        menu("Home")
        menu("Playground")

    search()
    copilot()
    chat()
    insights()
    stt()
    agents()

def set_page(main_page):
    global page
    page = main_page 