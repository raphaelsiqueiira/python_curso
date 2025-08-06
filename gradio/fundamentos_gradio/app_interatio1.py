import gradio as gr


def converter_temperatura(temperatura, escala):
    if escala == "Celsius":
        resultado = (temperatura * 9 / 5) + 32
        return f"{resultado:.2f} °F"
    else:  # Fahrenheit
        resultado = (temperatura - 32) * 5 / 9
        return f"{resultado:.2f} °C"


iface = gr.Interface(
    fn=converter_temperatura,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(choices=["Celsius", "Fahrenheit"], label="Converter de"),
    ],
    outputs=gr.Text(label="Resultado"),
    title="Conversor de Temperatura",
    description="Converte temperaturas entre Celsius e Fahrenheit",
)

iface.launch()
