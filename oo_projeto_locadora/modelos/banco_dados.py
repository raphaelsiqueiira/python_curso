from modelos.filmes import Filme

filmes = []


def adicionar_filme(filme: Filme) -> None:
    """Adiciona um novo filme se ainda não existir pelo título"""
    if isinstance(filme, Filme) and buscar_filme_por_titulo(filme.titulo) is None:
        filmes.append(filme)
    else:
        raise ValueError("Já existe um filme com esse título.")


def buscar_filme_por_titulo(titulo: str) -> Filme | None:
    """Busca um filme pelo título, ignorando maiúsculas e espaços"""
    titulo = titulo.strip().lower()
    for filme in filmes:
        if filme.titulo.lower() == titulo:
            return filme
    return None


def listar_todos_os_filmes() -> list[Filme]:
    """Retorna todos os filmes cadastrados"""
    return filmes[:]
