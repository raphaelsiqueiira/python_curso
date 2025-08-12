from modelos.item_locadora import ItemLocadora


class Filme(ItemLocadora):
    __slots__ = ("duracao",)

    def __init__(self, titulo: str, ano: int, duracao: float) -> None:
        super().__init__(titulo, ano)
        self._tipo = "Filme"
        self.duracao = duracao

    def __repr__(self):
        return f"[{self.__class__.__name__}] {self.id[:8]}  {self.titulo} ({self.ano}) - {self.status}"

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.titulo} ({self.ano}) - {self.status}"

    def exibir_detalhe(self):
        base = self.exibir_detalhe_base()
        return f"{base}Duração: {self.duracao} minutos\n"
