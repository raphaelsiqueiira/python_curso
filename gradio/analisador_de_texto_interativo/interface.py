import gradio as gr
from analise import analisar_texto

titulo = "Analisador de Texto Interativo"
descricao = (
    "Digite um texto, escolha uma transformação e veja uma análise completa "
    "com contagem de palavras, frases e frequência."
)

analisador_ui = gr.Interface(
    fn=analisar_texto,
    inputs=[
        gr.Textbox(lines=10, label="Digite seu texto aqui"),
        gr.Radio(
            choices=[
                "nenhuma",
                "Maiscúlas",
                "Minúsculas",
                "Titulo",
                "Capitalizado",
                "Reverso",
            ],
            label="Transformação no texto",
        ),
    ],
    outputs=gr.Textbox(label="Resultado da Análise"),
    title=titulo,
    description=descricao,
)

analisador_ui.launch()
