from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista


biblioteca_1 = Biblioteca("Locadora Central")
biblioteca_2 = Biblioteca("Locadora Rua Nova")

livro1 = Livro("Python Essencial ", "João Silva ", 45.0, 300)
livro1.aplicar_desconto()

revista1 = Revista("Ciência Hoje", "Maria Souza", 25, 12)
revista1.aplicar_desconto()

biblioteca_1.adicionar_item(livro1)
biblioteca_2.adicionar_item(revista1)
biblioteca_1.receber_avaliacao("Fulano", 10)


def main():
    Biblioteca.listar_bibliotecas()
    biblioteca_1.exibir_itens()
    biblioteca_2.exibir_itens()
    print()
    biblioteca_1.buscar_itens("Python")


if __name__ == "__main__":
    main()
