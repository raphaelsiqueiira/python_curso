from modelos.item_locadora import ItemLocadora


class Serie(ItemLocadora):
    __slots__ = ("temporada",)
    catalogo_serie = []

    def __init__(self, titulo: str, ano: int, temporada: int) -> None:
        super().__init__(titulo, ano)
        self._tipo = "Série"
        self.temporada = temporada
        Serie.catalogo_serie.append(self)

    def __repr__(self):
        return (
            f"[{self.tipo}] {self.id[:8]}  {self.titulo} ({self.ano}) - {self.status}"
        )

    def __str__(self) -> str:
        return f"[{self.tipo}] {self.titulo} ({self.ano}) - {self.status}"

    def exibir_detalhe(self):
        base = self.exibir_detalhe_base()
        return f"{base}Temporadas: {self.temporada}\n"
