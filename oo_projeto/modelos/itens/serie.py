from modelos.itens.item_locadora import ItemLocadora


class Serie(ItemLocadora):
    def __init__(self, titulo, diretor, preco, temporadas):
        super().__init__(titulo, diretor, preco)
        self.temporadas = temporadas

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.05
