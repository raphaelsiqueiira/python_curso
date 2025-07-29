from modelos.item_locadora import ItemLocadora


class Filme(ItemLocadora):
    def __init__(self, titulo: str, ano: int, genero: str) -> None:
        super().__init__(titulo, ano)
        self.genero = genero.strip().title()

    def __str__(self) -> str:
        return f"[Filme] {self.titulo} ({self.ano}) - {self.genero}"

    def exibir_detalhes(self) -> str:
        """Retorna os detalhes do filme, como titulo, ano, genero, nota e status"""
        media = self.media_avaliacoes()
        media_str = f"{media:.2f}" if media is not None else "Sem avaliações"
        return (
            f"{self.titulo} ({self.ano})\n"
            f"Gênero: {self.genero}\n"
            f"Avaliação Média: {media_str}\n"
            f"Status: {self.status}"
        )
