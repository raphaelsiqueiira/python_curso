import gradio as gr
import numpy as np
from PIL import Image
import io
import base64
import html


def criar_slide(titulo, texto, imagem, cor_fundo, cor_texto):
    estilo = (
        f"background-color: {cor_fundo}; "
        f"color: {cor_texto}; "
        "padding:20px; "
        "text-align: center;"
    )

    # Escapa caracteres especiais
    titulo = html.escape(titulo)
    texto = html.escape(texto)

    imagem_html = ""
    if imagem is not None:
        buffered = io.BytesIO()
        Image.fromarray(imagem).save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        imagem_html = (
            f"<img src='data:image/png;base64,{img_str}' "
            "style='max-width: 100%; height: auto;'>"
        )

    slide_html = f"""
    <div style="{estilo}">
        <h1>{titulo}</h1>
        <p>{texto}</p>
        {imagem_html}
    </div>
    """
    return slide_html


iface = gr.Interface(
    fn=criar_slide,
    inputs=[
        gr.Textbox(label="Título do slide", placeholder="Digite o título..."),
        gr.Textbox(label="Texto do slide", placeholder="Digite o texto..."),
        gr.Image(type="numpy", label="Imagem do slide"),
        gr.ColorPicker(label="Cor de fundo"),
        gr.ColorPicker(label="Cor do texto"),
    ],
    outputs=gr.HTML(label="Slide customizado"),
    title="Criador de Slides",
    description="Crie um slide personalizado com título, texto, imagem e cores.",
)

iface.launch()
