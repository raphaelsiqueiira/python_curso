import gradio as gr


def somar(num1=0, num2=0) -> int | float:
    return num1 + num2


iface = gr.Interface(
    fn=somar,
    inputs=["number", "number"],
    outputs="number",
    title="Calculadora de Soma",
    description="Insira dois números para obter a soma",
    theme="default",
)

iface.launch()
