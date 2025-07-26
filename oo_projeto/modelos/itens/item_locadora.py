from abc import ABC, abstractmethod


class ItemLocadora(ABC):
    def __init__(self, titulo, diretor, preco):
        self._titulo = titulo
        self._diretor = diretor
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass
