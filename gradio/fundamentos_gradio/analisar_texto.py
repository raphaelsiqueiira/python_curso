import gradio as gr
import string
from collections import Counter

string_teste = "Python é bacana"
string_vazia = ""


def limpar_texto(texto: str) -> str:
    """Pega um testo e remove os espaços desnecessarios, deixa em minusculas. Depois remove as pontuações"""
    texto = texto.strip()
    texto = " ".join(texto.lower().split())
    return texto.translate(str.maketrans("", "", string.punctuation))


def frequencia_palavras(texto: str) -> Counter:
    """Recebe um texto e retorna a quantidade de vezes que as palavras apareceram"""
    texto_limpo = limpar_texto(texto)
    lista_palavras = texto_limpo.split()
    return Counter(lista_palavras)


def frequencia_caracteres(texto):
    """Recebe um texto e retorna a quantidade de vezes que um caracterer apareceu. Exclui espaços"""
    texto_limpo = limpar_texto(texto)
    somente_letras = "".join([c for c in texto_limpo if c.isalpha()])
    return Counter(somente_letras)


def contar_total_palavras(texto: str) -> int:
    """Recebe um texto e conta quantas paalvras tem"""
    texto_limpo = limpar_texto(texto)
    return len(texto_limpo.split())


def contar_total_caracteres(texto: str) -> int:
    """Recebe um texto e conta a quantidade de caracteres"""
    texto_sem_pontuacao = texto.translate(str.maketrans("", "", string.punctuation))
    return len(texto_sem_pontuacao)


def analisar_texto(texto: str) -> dict:
    texto_limpo = limpar_texto(texto)
    freq_palavras = frequencia_palavras(texto)
    freq_caracteres = frequencia_caracteres(texto)
    total_palavras = contar_total_palavras(texto)
    total_caracteres = contar_total_caracteres(texto)

    dicionario_texto_analisado = {
        "Total de Palavras": total_palavras,
        "Total de Caracteres": total_caracteres,
        "Frequência de Palavras": freq_palavras,
        "Frequência de Letras": freq_caracteres,
        "Texto Limpo": texto_limpo,
    }
    return dicionario_texto_analisado


def limpar_campos():
    return "", {}


with gr.Blocks() as demo:
    textbox_entrada = gr.Textbox(
        label="Texto a ser analisado", lines=5, placeholder="Digite seu texto aqui..."
    )
    saida_json = gr.JSON()
    btn_analisar = gr.Button("Analisar Texto")
    btn_limpar = gr.Button("Limpar Texto")

    btn_analisar.click(fn=analisar_texto, inputs=textbox_entrada, outputs=saida_json)
    btn_limpar.click(fn=limpar_campos, inputs=[], outputs=[textbox_entrada, saida_json])

demo.launch()
