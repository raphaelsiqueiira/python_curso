import re


def explorar_expressao_regular(texto):
    padrao = r"\bPython\b"
    if re.search(padrao, texto):
        print("O padrão foi encontrado no texto.")
    else:
        print("O padrão não foi encontrado no texto.")

    padrao_email = r"[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(padrao_email, texto)
    print(f"E-mails encontrados: {emails}")

    # Substiruir um padrão por outro
    texto_substituido = re.sub(r"Python", "Javascript", texto)
    print(texto_substituido)

    # Dividir uma string com base em um padrão
    texto_dividido = re.split(r"\s+", texto)
    print(texto_dividido)


texto_exemplo = """
Olá, sou um desenvolvedor Python.
Você pode me contatar em meu e-mail: exemplo@dominio.com
Python é uma linguagem de programação popular.
"""

explorar_expressao_regular(texto_exemplo)
