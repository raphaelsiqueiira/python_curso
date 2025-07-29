import os
import time
from modelos.banco_dados import Filme


def limpar_tela():
    """Limpa o terminal/console"""
    os.system("cls" if os.name == "nt" else "clear")


def entrada_validada(msg: str, opcoes_validas: list[str]) -> str:
    """Valida a entrada para voltar ao loop anterior ou pedir novamente"""
    while True:
        resposta = input(msg).strip().lower()
        if resposta in opcoes_validas:
            return resposta
        elif resposta == "voltar":
            return "voltar"
        else:
            print("Entrada inválida. Tente novamente.")
            time.sleep(1)
            limpar_tela()


def mostrar_filmes(filmes: list[Filme]) -> None:
    """Exibe os detalhes de todos os filmes da lista fornecida."""
    for index, filme in enumerate(filmes, start=1):
        print(f"\nFILME {index}")
        print(filme.exibir_detalhes())
        print("-" * 40)
