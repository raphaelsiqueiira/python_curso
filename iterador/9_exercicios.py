import re


def extrair_urls(texto):
    padrao_url = r"https?://[a-zA-Z0-9.-]+\.[a-zA-z]{2,}"
    urls = re.findall(padrao_url, texto)
    return urls


texto_exemplo = """
Visite nosso site em https://www.exemplo.com e http://blog.exemplo.org para mais informações.
Entre em contato conosco em https://contto.exemplo.com.br
"""

urls_encontradas = extrair_urls(texto_exemplo)
print(urls_encontradas)


def validar_senha(senha):
    padrao_senha = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    return bool(re.match(padrao_senha, senha))


senhas = ["Senha123", "senha123", "SENHA123", "Senha!", "Valida1"]

for s in senhas:
    print(f"A senha {s} é valida? {validar_senha(s)}")


def contar_palavras(texto):
    padrao_palavra = r"\b\w+\b"
    palavras = re.findall(padrao_palavra, texto)
    return len(palavras)


texto_exemplo = "Olá, Mundo! Está é uma frase de exmplo para contar palavras"

numero_palavras = contar_palavras(texto_exemplo)
print(numero_palavras)
