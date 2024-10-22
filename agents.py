import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

page = None

def change_frame(menu):
       page.get_by_test_id("stSidebarUserContent").frame_locator("[data-testid=\"stCustomComponentV1\"]").get_by_role("link", name=menu).click() 

def press_enter():
    page.get_by_label("Selected Fortics. Modelo").press("Enter")

def save_inteligence():
     page.get_by_role("button", name="save icon 1").click()
    
def save_agent():
    page.get_by_role("button", name="save icon Salvar").click()

def description():
    page.locator("div").filter(has_text=re.compile(r"^Fortics$")).first.click()
    page.get_by_label("Selected Fortics. Modelo").fill("modelo de te")
    page.get_by_label("Selected Fortics. Modelo").press("Enter")

    page.get_by_test_id("stForm").get_by_label("Descrição").clear()
    page.get_by_test_id("stForm").get_by_label("Descrição").fill("Conteúdos sobre o GOgenier e Fortics")
    page.get_by_role("button", name="save icon 1").click()

def create_agent(name):
    change_frame("Cadastro de agentes")
    add = page.locator('button[data-testid="stBaseButton-secondary"]').nth(0).click()
    name = page.get_by_label("De um nome para seu agente").fill(name)
    save = page.get_by_test_id("stDialog").get_by_test_id("stBaseButton-secondary").click()
    time.sleep(3)
    config = page.get_by_text("settings_applicationsConfigurações do agente").click()
    llm = page.get_by_text("OpenAI").click()
    time.sleep(1)
    apikey = page.get_by_placeholder("<Cole aqui sua api_key>").fill("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")
    time.sleep(2)
    
def rules(rules):
    page.get_by_label("Outras regras e instruções").fill(rules)

def consultation():
    consultation = page.get_by_role("button", name="manage_search icon").click()
    # page.get_by_test_id("stDialog").get_by_test_id("stSelectbox").locator("div").filter(has_text="Escolha uma coleção").nth(2).click()
    collection = page.get_by_label("Coleção").fill("medico")
    page.get_by_label("Coleção").press("Enter")
    save_collection = page.get_by_test_id("stBaseButton-secondary").click()

def register():
    register = page.get_by_role("button", name="manage_search icon").click()
    collection = page.get_by_label("Coleção").fill("Clientes")
    page.get_by_label("Coleção").press("Enter")
    fields = page.get_by_label("Selecione os campos").fill("nome")
    page.get_by_label("Selecione os campos").press("Enter")
    save_collection = page.get_by_test_id("stBaseButton-secondary").click()

def config_flow():
    page.get_by_label("Caminho (proxy)").fill("/playwright/")


def add_inteligence(inteligence):
    page.get_by_label("Tipo de ação").fill(inteligence)
    page.get_by_label("Tipo de ação").press("Enter")
    page.get_by_role("button", name="add icon").click()

    if inteligence == "Utilizar modelo":
        description()
    elif inteligence == "Data e hora":
        rules("offset de -3")
    elif inteligence == "Busca em banco de da":
        rules("Responda tudo que o usuário solicitar")
        consultation()
    elif inteligence == "Insere em banco de da" :
        rules("Registre o usuario no banco de dados")
        register()
    elif inteligence == "Genier":
        config_flow()

    save_inteligence()
    


def create_agent_with_model():
    create_agent("Agente de teste com modelo")
    add_inteligence("Utilizar modelo")
    save_agent()

def create_agent_with_dataset():
    create_agent("Agente de teste com dataset")
    add_inteligence("Data e hora")
    save_agent()

def create_agent_with_consultation_database():
    create_agent("Agente de consulta database")
    add_inteligence("Busca em banco de da")
    save_agent()

def create_agent_with_register_database():
    create_agent("Agente de cadastro database")
    add_inteligence("Insere em banco de da")
    save_agent()

def create_agent_with_cnpj():
    create_agent("Agente de teste CNPJ")
    add_inteligence("Validação de CN")
    save_agent()

def create_agent_with_flow():
    create_agent("Agente de teste Flow")
    add_inteligence("Genier")
    save_agent()


def manage_agents():
    change_frame("Agente")

    # create_agent_with_model()
    # create_agent_with_dataset()
    # create_agent_with_consultation_database()
    # create_agent_with_register_database()
    # create_agent_with_cnpj()
    create_agent_with_flow()










def set_page(main_page):
    global page
    page = main_page   