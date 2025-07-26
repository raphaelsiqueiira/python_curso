from modelos.itens.item_locadora import ItemLocadora


class Filme(ItemLocadora):
    def __init__(self, titulo, autor, preco, duracao):
        super().__init__(titulo, autor, preco)
        self.duracao = duracao

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.10
