import gradio as gr


def reverter_texto(texto: str = "Texto") -> str:
    texto_revertido = texto[::-1]
    return texto_revertido, len((texto_revertido.replace(" ", "")))


iface = gr.Interface(
    fn=reverter_texto,
    inputs="text",
    outputs=["text", "number"],
    title="Reversor de Texto",
    description="Insira um texto para revertê-lo e contar os caracteres",
    theme="default",
)


iface.launch()
