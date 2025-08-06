import gradio as gr
import string
from collections import Counter


def converter_temperatura(temperatura, escala):
    if escala == "Celsius":
        resultado = (temperatura * 9 / 5) + 32
        return f"{resultado:.2f} °F"
    else:  # Fahrenheit
        resultado = (temperatura - 32) * 5 / 9
        return f"{resultado:.2f} °C"


def analisar_texto(texto):
    texto_limpo = texto.translate(str.maketrans("", "", string.punctuation))
    palavras = texto_limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    
    # Frequência formatada em Markdown, não HTML
    frequencia_md = "\n".join(
        [f"- **{palavra}**: {contagem}" for palavra, contagem in Counter(palavras).items()]
    )

    return num_palavras, num_caracteres, frequencia_md


def criar_relatorio(temperatura, escala, condicao, texto):
    temperatura_convertida = converter_temperatura(temperatura, escala)
    num_palavras, num_caracteres, frequencia = analisar_texto(texto)

    relatorio = (
        f"**Relatório de Clima**\n\n"
        f"- **Temperatura**: {temperatura_convertida} ({'F' if escala == 'Celsius' else 'C'})\n"
        f"- **Condição**: {condicao}\n"
        f"- **Descrição**: {texto}\n\n"
        f"**Análise do Texto**\n"
        f"- Número de Palavras: {num_palavras}\n"
        f"- Número de Caracteres: {num_caracteres}\n\n"
        f"**Frequência de Palavras:**\n{frequencia}"
    )
    return relatorio


iface = gr.Interface(
    fn=criar_relatorio,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(choices=["Celsius", "Fahrenheit"], label="Converter de"),
        gr.Dropdown(
            choices=["Ensolarado", "Nublado", "Chuvoso", "Frio", "Quente"],
            label="Condição do Clima",
        ),
        gr.Textbox(label="Descrição do Dia", lines=4, placeholder="Descreva o dia"),
    ],
    outputs=gr.Markdown(label="Relatório de Clima"),
    title="Relatório de Clima",
    description="Crie um relatório de clima com temperatura e análise textual.",
)
iface.launch()
