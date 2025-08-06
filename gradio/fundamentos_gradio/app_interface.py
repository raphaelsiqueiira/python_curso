import gradio as gr
import html

def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, estilo_fonte):
    estilo = (
        f"color: {cor_texto};"
        f"background-color: {cor_fundo};"
        f"font-size: {tamanho_fonte}px;"
        f"font-family: {estilo_fonte};"
    )
    texto_escapado = html.escape(texto)
    return f'<div style="{estilo}">{texto_escapado}</div>'

iface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite seu texto aqui..."),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor de Texto"),
        gr.Slider(minimum=10, maximum=100, step=1, value=20, label="Tamanho da Fonte"),
        gr.Radio(choices=["Arial", "Courier New", "Roboto"], label="Estilo da Fonte"),
    ],
    outputs=gr.HTML(label="Texto Customizado"),
    title="Customizador de texto",
    description="Customize o seu texto com cor, tamanho e estilo da fonte.",
)

iface.launch()
