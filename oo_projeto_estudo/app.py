from modelos.menu import menu_principal
from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_teste = Biblioteca("Locadora Central")

livro1 = Livro("Dom Casmurro", "Machado de Assis", 39.90, 256)
livro1.aplicar_desconto()

livro2 = Livro("1984", "George Orwell", 42.50, 328)


revista1 = Revista(
    "Revista Ciência Hoje",
    "Sociedade Brasileira para o Progresso da Ciência",
    18.00,
    134,
)
revista2 = Revista(
    "Revista Literatura Brasileira", "Academia Brasileira de Letras", 22.00, 87
)
revista2.aplicar_desconto()

biblioteca_teste.adicionar_item(livro1)
biblioteca_teste.adicionar_item(livro2)
biblioteca_teste.receber_avaliacao("Fulano", 10)

biblioteca_teste.adicionar_item(revista1)
biblioteca_teste.adicionar_item(revista2)


def main():
    menu_principal()


if __name__ == "__main__":
    main()
