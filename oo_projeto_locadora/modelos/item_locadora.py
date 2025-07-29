from abc import ABC, abstractmethod
from typing import Optional


class ItemLocadora(ABC):
    def __init__(self, titulo: str, ano: int) -> None:
        self.titulo = titulo.strip().title()
        self.ano = ano
        self._alugado = False
        self._avaliacoes: list[int] = []

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.titulo} ({self.ano})"

    @property
    def alugado(self) -> bool:
        return self._alugado

    @property
    def status(self) -> str:
        return "Alugado" if self._alugado else "Disponível"

    @property
    def avaliacoes(self) -> list[int]:
        return self._avaliacoes[:]

    def alugar(self) -> str:
        """Marca um item como alugado, se disponível"""
        if not self.alugado:
            self._alugado = True
            return f"Filme {self.titulo} alugado com sucesso!"
        else:
            return f"O filme {self.titulo} já está alugado."

    def devolver(self) -> str:
        """Devolve um item, se ele estiver alugado"""
        if self.alugado:
            self._alugado = False
            return f"O filme {self.titulo} foi devolvido."
        else:
            return f"O filme {self.titulo} não está alugado para ser devolvido."

    def avaliar(self, nota: int) -> None:
        """Adiciona uma avaliação de 1 a 5 para um item"""
        if not 1 <= nota <= 5:
            raise ValueError("Nota inválida! Digite um valor de 1 a 5.")
        self._avaliacoes.append(nota)

    def media_avaliacoes(self) -> Optional[float]:
        """Retorna a média das avaliações ou None se não houver"""
        if not self.avaliacoes:
            return None
        return round(sum(self.avaliacoes) / len(self.avaliacoes), 2)

    @abstractmethod
    def exibir_detalhes(self) -> str:
        pass
