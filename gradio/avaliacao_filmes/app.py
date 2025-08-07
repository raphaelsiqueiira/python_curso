import gradio as gr
from datetime import date
from modelos.filmes import Filme
from modelos.series import Serie

ano_atual = date.today().year

catalogo = []


def cadastrar_item(tipo, titulo, ano, duracao, temporada):
    tipo = tipo

    if not titulo.strip():
        return "O campo 'Título' é obrigatório."

    elif not ano:
        return "O campo 'Ano de Lançamento' é obrigatório."

    try:
        ano = int(ano)
        if tipo == "filme":
            duracao = float(duracao)
        elif tipo == "série":
            temporada = int(temporada)
    except (ValueError, TypeError):
        return "Erro ao converter os dados numéricos. Verifique os campos."

    if not (1800 <= ano <= ano_atual):
        return f"O campo 'Ano' deve estar entre 1800 e {ano_atual}."

    if tipo == "Filme":
        if duracao < 0:
            return "Informe uma duração válida para o filme."
        novo = Filme(titulo, ano, duracao)
    elif tipo == "Série":
        if temporada < 0:
            return "Informe uma quantidade válida de temporadas para a série."
        novo = Serie(titulo, ano, temporada)
    else:
        return "Tipo de item inválido. Escolha entre 'Filme' ou 'Série'."

    catalogo.append(novo)

    return str(novo.exibir_detalhe())


def alternar_campos(opcao):
    return (
        gr.update(visible=(opcao == "Filme")),
        gr.update(visible=(opcao == "Série")),
    )


with gr.Blocks() as demo:
    gr.Markdown("# Sistema de Gestão de Locadoras")

    with gr.Tabs():
        # TAB 1 - Cadastro
        with gr.Tab(label="Cadastro de Itens"):
            gr.Markdown("## Cadastro de Itens da Locadora")

            tipo = gr.Radio(
                ["Filme", "Série"], label="Tipo de Item (Obrigatório)", value="Filme"
            )
            titulo = gr.Textbox(label="Título (Obrigatório)")
            ano = gr.Number(label="Ano de Lançamento (Obrigatório)", value=ano_atual)

            duracao = gr.Number(label="Duração do Filme (min)", value=90, visible=True)
            temporada = gr.Number(
                label="Quantidade de Temporadas", value=1, visible=False
            )

            btn_cadastrar = gr.Button("Cadastrar")
            saida = gr.Textbox(label="Resultado", lines=6)

            btn_cadastrar.click(
                fn=cadastrar_item,
                inputs=[tipo, titulo, ano, duracao, temporada],
                outputs=saida,
            )

            tipo.change(
                alternar_campos,
                inputs=tipo,
                outputs=[duracao, temporada],
            )

        # TAB 2 - Catálogo
        with gr.Tab(label="Catálogo de Itens Cadastrados"):
            gr.Markdown("## Catálogo de Itens")
            opcoes = gr.Radio(
                ["Todos", "Filme", "Série"],
                label="Tipo de Item",
                value="Todos",
            )

if __name__ == "__main__":
    demo.launch()
