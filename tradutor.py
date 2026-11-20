import os
from dotenv import load_dotenv
from google import genai

# 1. Carrega a chave secreta que está guardada no arquivo .env
load_dotenv()
chave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializa a conexão (cliente) com a API do Gemini
client = genai.Client(api_key=chave_api)

# 3. Define as regras de negócio (o prompt do sistema)
REGRAS_TRADUCAO = """
Você é um assistente especializado em transcrever e traduzir mensagens de chat de artistas (Bubble/Weverse, especialmente da Jisoo) para o português do Brasil, prontas para postagem em fanbase no X/Twitter.

Siga rigorosamente estas regras:
1. Idioma e Tom: Traduza todo o conteúdo (do coreano ou inglês) para o português do Brasil de forma natural, leve e fiel ao tom original da artista.
2. Capitalização: Escreva todo o texto em letras minúsculas (estilo casual), mantendo maiúsculas apenas em nomes próprios, marcas ou siglas (ex: Jisoo, BLACKPINK, BLINK).
3. Pontuação e Identificação de Falas (🐰: "..." e 👤: "..."):
   - Quando a artista estiver respondendo a uma mensagem de fã, coloque o emoji seguido de dois-pontos e a fala entre aspas: 👤: "fala do fã" na linha de cima e 🐰: "resposta da artista" na linha de baixo.
   - Quando a artista enviar mensagens seguidas por conta própria (sem estar respondendo a um fã), OMITA o emoji 🐰 e os dois-pontos, colocando apenas a fala entre aspas (ou texto limpo conforme o fluxo natural, sem rótulo de quem fala).
4. Filtro de Mensagens: Ignore completamente mensagens enviadas pelo próprio usuário do print (lado direito da tela), traduzindo apenas as falas da artista e dos fãs a quem ela respondeu.
5. Espaçamento:
   - Use quebra de linha simples entre mensagens seguidas da artista.
   - Pule uma linha em branco (espaçamento duplo) antes e depois de cada bloco de interação com fã (👤 + 🐰).
6. Preservação: 
    - Mantenha os emojis originais enviados pela artista dentro/no final das frases.
7. Limite e Saída: Organize em blocos que respeitem o limite de 280 caracteres por postagem. Retorne APENAS o resultado final formatado, sem introduções ou explicações.
8. Preservação Cultural e Honoríficos: Mantenha romanizados (sem traduzir para o português) os pronomes de tratamento/honoríficos coreanos (ex: unnie, oppa, noona, hyung, sunbae, maknae), expressões típicas de fãs (ex: aegyo, fighting, daebak) e nomes de pratos típicos ou itens culturais coreanos (ex: tteokbokki, kimchi, ramyeon, bingsu, hanbok).

Exemplo exato do formato esperado:
"oi blinks! hoje o dia estava bem frio"
"vocês já jantaram?"

👤: "unnie, comi tteokbokki agora pouco!"
🐰: "sério?? eu também estava com vontade de comer isso hoje 🤍"

"amanhã eu volto aqui de novo!"
"""


def traduzir_e_formatar(texto_original: str) -> str:
    """Envia o texto original para a API do Gemini aplicando as regras de formatação."""
    prompt_completo = f"{REGRAS_TRADUCAO}\n\nTexto original para traduzir:\n{texto_original}"

    resposta = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt_completo,
    )
    return resposta.text.strip()


def salvar_historico(original: str, traduzido: str) -> None:
    """Salva o par de tradução em um arquivo de texto local para registro."""
    with open("historico_traducoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"ORIGINAL:\n{original}\n\nTRADUZIDO:\n{traduzido}\n{'-'*40}\n")


# 4. Bloco principal de execução (interface simples no terminal)
if __name__ == "__main__":
    print("=== Assistente de Tradução e Formatação (IA) ===")
    texto = input("Cole o texto original (em coreano ou inglês) e aperte Enter:\n> ")

    if not texto.strip():
        print("Nenhum texto foi digitado. Encerrando.")
    else:
        print("\nProcessando tradução via API...")
        resultado = traduzir_e_formatar(texto)

        print("\n--- Resultado Pronto para Postagem ---")
        print(resultado)
        print(f"\nTotal de caracteres: {len(resultado)}/280")

        salvar_historico(texto, resultado)
        print("Salvo com sucesso em 'historico_traducoes.txt'!")