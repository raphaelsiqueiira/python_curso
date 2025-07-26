from modelos.itens.item_biblioteca import ItemBiblioteca


class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, edicoes):
        super().__init__(titulo, autor, preco)
        self.edicoes = edicoes

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.05
