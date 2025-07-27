from modelos.avaliacao import Avaliacao
from modelos.itens.item_biblioteca import ItemBiblioteca


class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome

    @classmethod
    def criar_biblioteca(cls, nome_biblioteca):
        nome_biblioteca = nome_biblioteca.title().strip()
        if nome_biblioteca in [b.nome for b in Biblioteca.bibliotecas]:
            print(
                f"Já existe uma  biblioteca chamada {nome_biblioteca}. Digite outro nome"
            )
            return None
        return cls(nome_biblioteca)

    @classmethod
    def remover_biblioteca(cls, indice_biblioteca):
        try:
            indice_biblioteca = int(indice_biblioteca)
            if 0 <= indice_biblioteca - 1 < len(cls.bibliotecas):
                biblioteca_removida = cls.bibliotecas.pop(indice_biblioteca - 1)
                return f"Biblioteca '{biblioteca_removida.nome}' removida com sucesso!"
            else:
                return f"Índice {indice_biblioteca} inválido."
        except (ValueError, IndexError):
            return "Erro: insira um número válido para o índice da biblioteca."

    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)

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

    def exibir_itens(self):
        print(f"\nItens da Biblioteca {self.nome}")
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, "paginas"):
                msg_filme = f"{i} - (LIVRO) Título: {item._titulo.ljust(30)} | Autor: {item._autor.ljust(30)} | Preço: R$ {str(item._preco).ljust(10)} | Páginas: {item.paginas}"
                print(msg_filme)

            else:
                msg_serie = f"{i} - (REVISTA) Título: {item._titulo.ljust(30)} | Autor: {item._autor.ljust(30)} | Preço: R$ {str(item._preco).ljust(10)} | Edições: {item.edicoes}"
                print(msg_serie)

    @classmethod
    def alterar_status_biblioteca(cls, indice_biblioteca):
        try:
            indice_biblioteca = int(indice_biblioteca)
            if 0 <= indice_biblioteca - 1 < len(cls.bibliotecas):
                biblioteca_alterada = cls.bibliotecas[indice_biblioteca - 1]
                biblioteca_alterada.alternar_status()

                return f"Biblioteca '{biblioteca_alterada.nome}' teve o status atualizado para {biblioteca_alterada.ativo}!"
            else:
                return f"Índice {indice_biblioteca} inválido."
        except (ValueError, IndexError):
            return "Erro: insira um número válido para o índice da biblioteca."

    def alternar_status(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"

    @classmethod
    def listar_bibliotecas(cls):
        if not cls.bibliotecas:
            return "Nenhuma biblioteca cadastrada."

        linhas = [
            f"{'Nome da Biblioteca'.ljust(35)} | {'Nota média'.ljust(25)} | {'Status'}"
        ]
        for index, biblioteca in enumerate(cls.bibliotecas, start=1):
            linha = (
                f"{index} - {biblioteca.nome.ljust(31)} | "
                f"{str(biblioteca.media_avaliacoes).ljust(25)} | "
                f"{biblioteca.ativo}"
            )
            linhas.append(linha)

        return "\n".join(linhas)

    def buscar_itens(self, termo_busca):
        termo_busca = termo_busca.lower()
        resultados = [
            item for item in self._itens if termo_busca in item._titulo.lower()
        ]

        if not resultados:
            print(f"\nNenhum item encontrado com o termo '{termo_busca}'.")
            return

        print(f"\nItens encontrados com o termo '{termo_busca}':")

        for i, item in enumerate(resultados, start=1):
            if hasattr(item, "paginas"):
                print(
                    f"{i} - (Livro)   Título: {item._titulo.ljust(30)} | "
                    f"Autor: {item._autor.ljust(25)} | "
                    f"Preço: R$ {str(item._preco).ljust(10)} | "
                    f"Páginas: {item.paginas}"
                )
            else:
                print(
                    f"{i} - (Revista) Título: {item._titulo.ljust(30)} | "
                    f"Autor: {item._autor.ljust(25)} | "
                    f"Preço: R$ {str(item._preco).ljust(10)} | "
                    f"Edições: {item.edicoes}"
                )
