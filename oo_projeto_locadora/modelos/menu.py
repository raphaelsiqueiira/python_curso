from modelos import banco_dados
from modelos.filmes import Filme
from modelos.utils import entrada_validada, limpar_tela, mostrar_filmes
import time


def mostrar_menu():
    while True:
        limpar_tela()
        print(" SISTEMA LOCADORA ".center(40, "="))
        print(
            "1 - Cadastrar filme\n"
            "2 - Listar todos os filmes\n"
            "3 - Buscar filme por título\n"
            "4 - Avaliar filme\n"
            "5 - Alugar filme\n"
            "6 - Devolver filme\n"
            "7 - Sair\n"
        )

        escolha_menu = entrada_validada(
            "Digite sua escolha:\n>>> ", ["1", "2", "3", "4", "5", "6", "7"]
        )

        limpar_tela()

        if escolha_menu == "1":
            while True:
                titulo = input(
                    "Digite o título do filme (ou 'voltar' para retornar ao menu):\n>>> "
                ).strip()
                if titulo.lower() == "voltar":
                    break
                if not titulo:
                    print("Campo 'título' vazio! Tente novamente.")
                    time.sleep(1.5)
                    continue

                try:
                    ano_str = input(
                        "Digite o ano de lançamento do filme (ou 'voltar' para retornar):\n>>> "
                    ).strip()
                    if ano_str.lower() == "voltar":
                        break
                    ano = int(ano_str)
                except ValueError:
                    print("Ano inválido! Digite um número válido.")
                    time.sleep(1.5)
                    continue

                genero = input(
                    "Digite o gênero do filme (ou 'voltar' para retornar):\n>>> "
                ).strip()
                if genero.lower() == "voltar":
                    break
                if not genero:
                    print("Campo 'gênero' vazio! Tente novamente.")
                    time.sleep(1.5)
                    continue

                novo_filme = Filme(titulo, ano, genero)
                try:
                    banco_dados.adicionar_filme(novo_filme)
                    print(f"Filme '{titulo}' cadastrado com sucesso.")
                    time.sleep(2)
                    break
                except ValueError as e:
                    print(e)
                    time.sleep(2)
                    break

        elif escolha_menu == "2":
            filmes_cadastrados = banco_dados.listar_todos_os_filmes()
            if not filmes_cadastrados:
                print("Nenhum filme cadastrado ainda.")
            else:
                mostrar_filmes(filmes_cadastrados)
            input("\nPressione Enter para voltar ao menu...")

        elif escolha_menu == "3":
            while True:
                titulo = input(
                    "Digite o título do filme que procura (ou 'voltar' para retornar):\n>>> "
                ).strip()
                if titulo.lower() == "voltar":
                    break
                if not titulo:
                    print("Campo vazio! Tente novamente.")
                    time.sleep(1.5)
                    continue

                filme_encontrado = banco_dados.buscar_filme_por_titulo(titulo)
                if filme_encontrado is None:
                    print("Nenhum filme foi encontrado com esse título.")
                else:
                    print("\nFILME ENCONTRADO:")
                    print(filme_encontrado.exibir_detalhes())

                input(
                    "\nPressione Enter para buscar outro filme ou digite 'voltar' para sair."
                )
                limpar_tela()

        elif escolha_menu == "4":
            while True:
                filmes = banco_dados.listar_todos_os_filmes()
                if not filmes:
                    print("Nenhum filme disponível para avaliação.")
                    time.sleep(2)
                    break
                mostrar_filmes(filmes)

                titulo = input(
                    "Digite o título do filme que deseja avaliar (ou 'voltar'):\n>>> "
                ).strip()
                if titulo.lower() == "voltar":
                    break
                if not titulo:
                    print("Campo vazio! Tente novamente.")
                    time.sleep(1.5)
                    continue

                filme_encontrado = banco_dados.buscar_filme_por_titulo(titulo)
                if filme_encontrado is None:
                    print("Nenhum filme foi encontrado com esse título.")
                    time.sleep(1.5)
                    continue

                print("\nFILME ENCONTRADO:")
                print(filme_encontrado.exibir_detalhes())

                while True:
                    nota_str = input(
                        "Digite a nota do filme (1 a 5) ou 'voltar' para cancelar:\n>>> "
                    ).strip()
                    if nota_str.lower() == "voltar":
                        break
                    try:
                        nota = int(nota_str)
                        filme_encontrado.avaliar(nota)
                        print(
                            f"O filme '{filme_encontrado.titulo}' recebeu a nota {nota}!"
                        )
                        time.sleep(2)
                        break
                    except ValueError as e:
                        print(f"Erro ao avaliar: {e}")
                        time.sleep(1.5)

                break

        elif escolha_menu == "5":
            while True:
                filmes = banco_dados.listar_todos_os_filmes()
                if not filmes:
                    print("Nenhum filme disponível para aluguel.")
                    time.sleep(2)
                    break
                mostrar_filmes(filmes)

                titulo = input(
                    "Digite o título do filme que deseja alugar (ou 'voltar'):\n>>> "
                ).strip()
                if titulo.lower() == "voltar":
                    break

                filme_encontrado = banco_dados.buscar_filme_por_titulo(titulo)
                if filme_encontrado is None:
                    print("Filme não encontrado. Tente novamente.")
                    time.sleep(1.5)
                    limpar_tela()
                    continue

                print(filme_encontrado.exibir_detalhes())
                confirmacao = entrada_validada(
                    "Confirmar aluguel? (s/n ou 'voltar'):\n>>> ",
                    ["s", "sim", "n", "nao", "não"],
                )
                if confirmacao in ["s", "sim"]:
                    print(filme_encontrado.alugar())
                    time.sleep(2)
                    break
                elif confirmacao == "voltar":
                    break
                else:
                    print("Aluguel cancelado.")
                    time.sleep(1.5)
                    break

        elif escolha_menu == "6":
            while True:
                filmes = banco_dados.listar_todos_os_filmes()
                if not filmes:
                    print("Nenhum filme disponível para devolver.")
                    time.sleep(2)
                    break
                mostrar_filmes(filmes)
                titulo = input(
                    "Digite o título do filme que deseja devolver (ou 'voltar'):\n>>> "
                ).strip()
                if titulo.lower() == "voltar":
                    break

                filme_encontrado = banco_dados.buscar_filme_por_titulo(titulo)
                if filme_encontrado is None:
                    print("Filme não encontrado. Tente novamente.")
                    time.sleep(1.5)
                    limpar_tela()
                    continue

                print(filme_encontrado.exibir_detalhes())
                confirmacao = entrada_validada(
                    "Confirmar devolução? (s/n ou 'voltar'):\n>>> ",
                    ["s", "sim", "n", "nao", "não"],
                )
                if confirmacao in ["s", "sim"]:
                    print(filme_encontrado.devolver())
                    time.sleep(2)
                    break
                elif confirmacao == "voltar":
                    break
                else:
                    print("Devolução cancelada.")
                    time.sleep(1.5)
                    break

        elif escolha_menu == "7":
            print("Encerrando o sistema. Até logo!")
            time.sleep(1)
            break
