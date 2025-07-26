from modelos.avaliacao import Avaliacao
from modelos.itens.item_locadora import ItemLocadora


class Locadora:
    locadoras = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        self._itens = []
        Locadora.locadoras.append(self)

    def __str__(self):
        return self.nome

    @classmethod
    def listar_locadora(cls):
        print(f"{'Nome da locadora'.ljust(25)} | {'Nota média'.ljust(25)} | {'Status'}")
        for locadora in Locadora.locadoras:
            print(
                f"{locadora.nome.ljust(25)} | {str(locadora.media_avaliacoes).ljust(25)} | {locadora.ativo}"
            )

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        return media

    def adicionar_item(self, item):
        if isinstance(item, ItemLocadora):
            self._itens.append(item)

    def exibir_itens(self):
        print(f"\nItens da Locadorada {self.nome}")
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, "duracao"):
                msg_filme = f"{i} - (Filme) Título: {item._titulo.ljust(30)} | Autor: {item._diretor.ljust(30)} | Preço: R$ {str(item._preco).ljust(10)} | Duração: {item.duracao} h"
                print(msg_filme)

            else:
                msg_serie = f"{i} - (Serie) Título: {item._titulo.ljust(30)} | Autor: {item._diretor.ljust(30)} | Preço: R$ {str(item._preco).ljust(10)} | Duração: {item.temporadas} Temporada(s)"
                print(msg_serie)
