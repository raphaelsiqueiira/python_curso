import string
from collections import Counter


def analisar_texto(texto, transformacao="nenhuma"):
    if transformacao == "Maiscúlas":
        texto_transformado = texto.upper()
    elif transformacao == "Minúsculas":
        texto_transformado = texto.lower()
    elif transformacao == "Titulo":
        texto_transformado = texto.title()
    elif transformacao == "Capitalizado":
        texto_transformado = texto.capitalize()
    elif transformacao == "Reverso":
        texto_transformado = texto[::-1]
    else:
        texto_transformado = texto

    texto_limpo = texto_transformado.translate(
        str.maketrans("", "", string.punctuation)
    )
    palavras = texto_limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    num_frases = texto.count(".") + texto.count("!") + texto.count("?")
    top_3 = Counter(palavras).most_common(3)
    frequencia_formatada = "\n".join(
        [f"{i+1}. Palavra: {palavra} - Contagem: {contagem}" for i, (palavra, contagem) in enumerate(top_3)]
    )

    resultado = f"""Análise do Texto:
- Total de palavras: {num_palavras}
- Total de caracteres: {num_caracteres}
- Total de frases: {num_frases}
- Top 3 palavras mais frequentes:
{frequencia_formatada}

- Texto transformado: {texto_transformado}
"""
    return resultado
