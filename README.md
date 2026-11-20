# Assistente de Tradução e Formatação para Redes Sociais (IA)

Ferramenta desenvolvida em Python que utiliza a API do Google Gemini para traduzir e formatar mensagens de artistas sul-coreanos (Bubble/Weverse) para o português do Brasil, prontas para publicação em comunidades de fãs no X/Twitter.

## O Problema Real
Na gestão diária de comunidades de fãs, traduzir mensagens do coreano/inglês exige manter um padrão editorial rigoroso: preservação de honoríficos e termos culturais, diferenciação visual entre falas da artista e dos fãs, limite de caracteres e tom casual. Fazer essa formatação manualmente consome tempo e gera inconsistências.

## Como a Solução Funciona
1. **Entrada:** O usuário insere o texto original no terminal.
2. **Processamento via API REST:** O script envia o texto para o modelo `gemini-3.8-flash` com regras específicas de *Prompt Engineering* (preservação de termos como *unnie*, *oppa*, *fighting*, formatação de diálogos com `👤:` e `🐰:`, letras minúsculas e limite de 280 caracteres).
3. **Saída e Registro:** Exibe o texto pronto para postagem, contabiliza os caracteres e salva um histórico local automaticamente.

## Tecnologias Utilizadas
* **Python 3**
* **Google GenAI SDK** (Integração com API REST de IA)
* **Python-dotenv** (Gerenciamento seguro de variáveis de ambiente)
* **Git & GitHub** (Controle de versão)

## Como Executar Localmente
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/assistente-traducao-ia.git](https://github.com/SEU-USUARIO/assistente-traducao-ia.git)