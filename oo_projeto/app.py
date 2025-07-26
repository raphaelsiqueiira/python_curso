from modelos.locadora import Locadora
from modelos.itens.filme import Filme
from modelos.itens.serie import Serie


locadora_1 = Locadora("Locadora Central")
locadora_2 = Locadora("Locadora Rua Nova")

filme1 = Filme("Batman Begins", "Christopher Nolan", 45.0, 2.20)
filme1.aplicar_desconto()
serie1 = Serie("The Flash", "Greg Berlanti", 25, 9)

filme2 = Filme("Homem-Aranha", "Sam Raimi", 50.0, 2.06)
serie2 = Serie("O Espetacular Homem-Aranha", "Greg Weisman", 25, 2)
serie2.aplicar_desconto()

locadora_1.adicionar_item(filme1)
locadora_1.adicionar_item(serie1)
locadora_1.receber_avaliacao("Fulano", 10)

locadora_2.adicionar_item(filme2)
locadora_2.adicionar_item(serie2)


def main():
    Locadora.listar_locadora()
    locadora_1.exibir_itens()
    locadora_2.exibir_itens()


if __name__ == "__main__":
    main()
