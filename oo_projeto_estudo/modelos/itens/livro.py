from modelos.itens.item_biblioteca import ItemBiblioteca


class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, paginas):
        super().__init__(titulo, autor, preco)
        self.paginas = paginas

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.15
