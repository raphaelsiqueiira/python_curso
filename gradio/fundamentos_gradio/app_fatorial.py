import gradio as gr
import math


def fatorial(num: int = 1) -> int:
    if num < 0:
        return "Fatorial não definido para números negativos"
    return math.factorial(num)


iface = gr.Interface(
    fn=fatorial,
    inputs="number",
    outputs="text",
    title="Calculadora de Fatorial",
    description="Insira um número para obter o fatorial",
    theme="default",
)

iface.launch()
