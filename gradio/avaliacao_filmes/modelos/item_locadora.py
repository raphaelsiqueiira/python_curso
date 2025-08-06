from abc import abstractmethod, ABC
from typing import Optional
import uuid


class ItemLocadora(ABC):
    __slots__ = (
        "_ItemLocadora__id",
        "_tipo",
        "titulo",
        "ano",
        "_alugado",
        "_avaliacoes",
        "genero",
    )

    def __init__(self, titulo: str, ano: int) -> None:
        self._ItemLocadora__id = str(uuid.uuid4())
        self._tipo: str = ""
        self.titulo = titulo
        self.ano = ano
        self._alugado: bool = False
        self._avaliacoes: list[int] = []
        self.genero: list[str] = []

    def __repr__(self):
        return f"[{self.__class__.__name__}] {self.titulo} ({self.ano}) - {self.status}"

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.titulo} ({self.ano}) - {self.status}"

    def __eq__(self, other):
        return isinstance(other, ItemLocadora) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, value):
        raise AttributeError("ID não pode ser modificado.")

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def alugado(self) -> bool:
        return self._alugado

    @property
    def status(self) -> str:
        return "Alugado" if self._alugado else "Disponível"
    


    @property
    def avaliacoes(self) -> list[int]:
        return self._avaliacoes[:]

    def media_avaliacoes(self) -> Optional[float]:
        """Retorna a média das avaliações ou None se não houver"""
        if not self._avaliacoes:
            return None
        return round(sum(self._avaliacoes) / len(self._avaliacoes), 2)

    def avaliar(self, nota: int) -> None:
        """Adiciona uma avaliação de 1 a 5 para um item"""
        if not 1 <= nota <= 5:
            raise ValueError("Nota inválida! Digite um valor de 1 a 5.")
        self._avaliacoes.append(nota)

    def alugar(self) -> str:
        if not self._alugado:
            self._alugado = True
            return f"{self.tipo} {self.titulo} alugado com sucesso!"
        return f"O {self.tipo.lower()} {self.titulo} já está alugado."

    def devolver(self) -> str:
        if self._alugado:
            self._alugado = False
            return f"O {self.tipo.lower()} {self.titulo} foi devolvido."
        return (
            f"O {self.tipo.lower()} {self.titulo} não está alugado para ser devolvido."
        )

    def exibir_detalhe_base(self) -> str:
        media = self.media_avaliacoes()
        media_str = f"{media:.2f}" if media is not None else "Sem avaliações"
        genero_str = ", ".join(self.genero) if self.genero else "Não Informado"
        return (
            f"Tipo: {self.tipo}\n"
            f"{self.titulo} ({self.ano})\n"
            f"Gênero: {genero_str}\n"
            f"Avaliação Média: {media_str}\n"
            f"Status: {self.status}\n"
        )
