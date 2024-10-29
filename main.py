import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import data_source as d
import models as m
import agents as a
import playground as p
import integration as i
import config as c
import login as l
from config import logout
import api 

def run(playwright: Playwright) -> None:
    #  Acessando o navegador Chromium para realizar os testes 
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1870, "height": 880})
    page = context.new_page()
    page.goto("https://app.genier.ai/qa/")

    # For para aplicar a funcao set_page em todos os arquivos py
    for j in [d,m,a,p,i,c,l]:
        j.set_page(page)

# ---------------------

# O código segue um roteiro de ações, primeiro serão executadas as API's no terminal após isso irá abrir o browser no endereço do GOgenier, e executar este roteiro:

# --> Executar o login 
# --> Entrar na fonte de dados, selecionar a "fonte de testes" e inputar todos os tipos de dados
# --> Entrar em modelos, criar o "Modelo de teste", com a "fonte de testes" e processa-lo
# --> Entrar em agentes, criar 3 agentes, (agente de dataset, cadastro e consulta no database e agente com flow + conteúdo + db), ou outras opções disponiveis no código
# --> Entrar no playground, e consultar: Search, Chat, Copilot, STT, Insights e Agentes
# --> Após as consultas, retornar a fonte de dados e remover os links WEB e links do Youtube
# --> Retornar ao mesmo modelo criado e reprocessa-lo
# --> Retornar ao playground e consultar o modelo no Search para validar se os dados foram removidos
# --> Entrar nas configuraçoes, alterar LLM para Gemini, e depois para OpenAi novamente
# --> Nas configurações alterar senha do usuário, e alterar novamente pra senha anterior
# --> Ao fim realizará um logout para encerrar os testes

# ---------------------


    # Chamada das funções que executam as ações, logar, mexer na fonte de dados, mexer nos modelos e etc...
    l.login("Automac@o123")
    d.manage_data()
    m.manage_model()
    a.manage_agents()
    p.play_ground()
    d.remove_data()
    m.reprocess()
    p.talk_to_model()
    c.change_llm()
    c.change_password()
    logout()

    # Timer pro navegador nao fechar diretamente
    time.sleep(1200)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
