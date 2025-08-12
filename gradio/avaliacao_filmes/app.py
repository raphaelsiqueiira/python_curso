import gradio as gr
from datetime import date
from modelos.filmes import Filme
from modelos.series import Serie
from modelos.item_locadora import ItemLocadora

ano_atual = date.today().year


def cadastrar_item(tipo, titulo, ano, duracao, temporada):
    tipo = tipo.strip().capitalize()

    if not titulo.strip():
        return "O campo 'Título' é obrigatório."
    if not ano:
        return "O campo 'Ano de Lançamento' é obrigatório."

    if not (1800 <= ano <= ano_atual):
        return "Informe um ano de lançamento válido."

    try:
        ano = int(ano)
        if tipo == "Filme":
            duracao = float(duracao)
            if duracao < 0:
                return "Informe uma duração válida para o filme."
            novo = Filme(titulo, ano, duracao)
        elif tipo == "Série":
            temporada = int(temporada)
            if temporada < 0:
                return "Informe uma quantidade válida de temporadas."
            novo = Serie(titulo, ano, temporada)
        else:
            return "Tipo inválido."
    except (ValueError, TypeError):
        return "Erro ao converter os dados numéricos."

    return str(novo.exibir_detalhe())


def alternar_campos(tipo):
    return (
        gr.update(visible=(tipo == "Filme")),
        gr.update(visible=(tipo == "Série")),
    )


def listar_catalogo(opcao):
    itens = ItemLocadora.listar_catalogo()

    if opcao == "Filmes":
        itens = [item for item in itens if isinstance(item, Filme)]
    elif opcao == "Séries":
        itens = [item for item in itens if isinstance(item, Serie)]

    if not itens:
        return "Nenhum Item Cadastrado"

    return "\n\n".join(i.exibir_detalhe() for i in itens)


def alternar_listagem(opcao):
    if opcao == "Todos":
        return gr.update(visible=(opcao == "Todos"))
    elif opcao == "Filmes":
        return gr.update(visible=(opcao == "Filmes"))
    elif opcao == "Series":
        return gr.update(visible=(opcao == "Séries"))


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
                ["Todos", "Filmes", "Séries"],
                label="Tipos de Item",
                value="Todos",
            )
            saida_catalogo = gr.Textbox(label="Itens Cadastrados", lines=15)

            opcoes.change(
                listar_catalogo,
                inputs=opcoes,
                outputs=saida_catalogo,
            )

if __name__ == "__main__":
    demo.launch()
