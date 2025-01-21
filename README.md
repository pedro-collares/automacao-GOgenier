# Automação de Testes no GOgenier

Este projeto executa uma série de ações automatizadas no site do GOgenier, seguindo um roteiro predefinido. O processo inclui a execução de APIs, navegação pelo site, criação e manipulação de dados e validação de resultados.

## Roteiro de Ações

1. **Execução de APIs**  
   Inicialmente, o código executa as APIs no terminal.

2. **Acesso ao GOgenier**  
   Após a execução das APIs, o navegador será aberto no endereço do GOgenier para executar as ações a seguir.

### Ações Automáticas no Site

- **Login:**  
  Realiza o login no sistema.

- **Fonte de Dados:**  
  - Acessa a "fonte de testes".
  - Insere todos os tipos de dados disponíveis.

- **Modelos:**  
  - Cria o "Modelo de teste" utilizando a "fonte de testes".
  - Processa o modelo criado.

- **Agentes:**  
  - Cria três agentes:
    1. Agente de dataset.
    2. Agente para cadastro e consulta no banco de dados.
    3. Agente com fluxo (flow), conteúdo e banco de dados.  
  - Alternativamente, outras opções disponíveis no código podem ser utilizadas.

- **Playground:**  
  - Realiza consultas nos módulos:
    - Search
    - Chat
    - Copilot
    - STT (Speech-to-Text)
    - Insights
    - Agentes

- **Fonte de Dados:**  
  - Retorna à fonte de dados para remover links WEB e links do YouTube.

- **Modelo:**  
  - Retorna ao modelo criado previamente e reprocessa-o.

- **Validação:**  
  - Retorna ao playground e consulta o modelo no módulo **Search** para verificar se os dados foram removidos.

- **Configurações:**  
  - Altera o modelo de LLM para **Gemini** e, em seguida, volta para **OpenAI**.
  - Modifica a senha do usuário e depois redefine para a senha original.

- **Logout:**  
  - Finaliza os testes realizando o logout do sistema.

---

Este roteiro foi projetado para validar funcionalidades específicas e garantir a consistência das operações no sistema. Certifique-se de que todas as dependências necessárias estejam configuradas antes de iniciar o processo.
