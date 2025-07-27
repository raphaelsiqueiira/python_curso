from modelos.biblioteca import Biblioteca
from modelos.utils import limpar_tela, pausar_tela
from time import sleep


def menu_principal():
    while True:
        limpar_tela()
        print(" GERENCIAMENTO DE BIBLIOTECAS ".center(50, "="), "\n")
        print(
            "Escolha uma das opções:\n(1) - Acessar Conta\n(2) - Criar Conta\n(3) - Sair\n"
        )
        escolha = input("Digite sua escolha:\n>>> ")
        sleep(1)

        match escolha:
            case "1":
                menu_usuario()
            case "2":
                print("Funcionalidade de criação de conta ainda não implementada.")
                sleep(2)
            case "3":
                confirmar_saida = input(
                    "Você tem certeza que deseja sair? (1 - Sim | 2 - Não)\n>>> "
                )
                if confirmar_saida == "1":
                    print("O programa será fechado. Até a próxima!\n")
                    sleep(2)
                    limpar_tela()
                    break
            case _:
                print("Opção inválida!")
                sleep(1)


def menu_usuario():
    while True:
        limpar_tela()
        print("Seja bem vindo {Usuário}!\n")
        print(
            "Escolha uma das opções:\n(1) - Criar biblioteca\n(2) - Listar bibliotecas\n(3) - Voltar\n"
        )
        escolha = input("Digite sua escolha:\n>>> ")

        match escolha:
            case "1":
                menu_criar_biblioteca()
            case "2":
                menu_listar_biblioteca()
            case "3":
                break
            case _:
                print("Opção inválida!")
                sleep(1)


def menu_criar_biblioteca():
    while True:
        limpar_tela()
        print(" CRIAR BIBLIOTECA ".center(50, "="), "\n")
        escolha = input(
            "Você deseja criar uma nova biblioteca?\n(1) - Criar\n(2) - Voltar\n>>> "
        )

        if escolha == "1":
            nome = input("Digite o nome da nova Biblioteca:\n>>> ").title()
            if not nome:
                print("Você não pode inserir um valor vazio!")
                pausar_tela()
                continue
            nova_biblioteca = Biblioteca.criar_biblioteca(nome)
            if nova_biblioteca:
                print(f"\nBiblioteca '{nova_biblioteca.nome}' criada com sucesso!")
            else:
                print("\nNão foi possível criar a biblioteca. Já existe com esse nome.")
            pausar_tela()
        elif escolha == "2":
            break
        else:
            print("Opção inválida!")
            sleep(1)


def menu_listar_biblioteca():
    while True:
        limpar_tela()
        print(" LISTAGEM BIBLIOTECAS ".center(50, "="), "\n")
        print(Biblioteca.listar_bibliotecas())
        print(
            "\nEscolha uma das opções:\n(1) - Consultar acervo da biblioteca\n(2) - Remover biblioteca\n(3) - Alterar status biblioteca\n(4) - Voltar\n"
        )
        escolha = input("Digite sua escolha:\n>>> ")
        if escolha == "1":
            indice = input(
                "Digite o índice da biblioteca que deseja visualizar os itens:\n>>> "
            )
            biblioteca = menu_acervo_bibliotecas(indice)
            if biblioteca:
                menu_opcoes_acervo_biblioteca(biblioteca)
                pausar_tela()
        elif escolha == "2":
            indice = input("Digite o índice da biblioteca que deseja remover:\n>>> ")
            mensagem = Biblioteca.remover_biblioteca(indice)
            print(mensagem)
            pausar_tela()

        elif escolha == "3":
            indice = input(
                "Digite o índice da biblioteca que deseja alterar o status:\n>>> "
            )
            mensagem = Biblioteca.alterar_status_biblioteca(indice)
            print(mensagem)
            pausar_tela()

        elif escolha == "4":
            break
        else:
            print("Opção inválida!")
            sleep(1)


def menu_acervo_bibliotecas(indice_biblioteca):
    try:
        indice_biblioteca = int(indice_biblioteca)
        if 0 <= indice_biblioteca - 1 < len(Biblioteca.bibliotecas):
            return Biblioteca.bibliotecas[indice_biblioteca - 1]
        else:
            print(f"Índice {indice_biblioteca} inválido.")
            return None
    except (ValueError, IndexError):
        print("Erro: insira um número válido para o índice da biblioteca.")
        return None


def menu_opcoes_acervo_biblioteca(biblioteca):
    while True:
        limpar_tela()
        print(f"ACERVO DA BIBLIOTECA: {biblioteca.nome}\n")
        biblioteca.exibir_itens()

        print(
            "\nEscolha uma das opções:\n"
            "(1) - Procurar item\n(2) - Criar novo item\n(3) - Remover um item\n(4) - Voltar"
        )
        escolha = input("Digite sua escolha:\n>>> ")

        if escolha == "1":
            termo = input("Digite o termo de busca:\n>>> ")
            biblioteca.buscar_itens(termo)
            pausar_tela()
        elif escolha == "2":
            print("Funcionalidade ainda não implementada.")
            pausar_tela()
        elif escolha == "3":
            print("Funcionalidade ainda não implementada.")
            pausar_tela()
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")
            sleep(1)
