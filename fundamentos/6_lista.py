"""
Objetivos da aula:
Entender o que são listas

Aprender indexação e fatiamento de listas

Usar métodos importantes (append, sort, remove, etc.)

Manipular listas na prática
"""

filme_batman = ["Batman Begins", 2005, 8.2, True]
"""
Aqui temos uma lista com múltiplos tipos de dados (str, int, float, bool). Isso é normal em Python, pois listas são estruturas heterogêneas.
"""

print(type(filme_batman))
print(filme_batman)

films_list = [
    "Batman Begins",
    "Sharknado",
    "O Menino do Pijama Listrado",
    "O Espetacular Homem Aranha",
]

# 1 - Buscar  os dois primeiros itens da lista
print(films_list[:2])

# 2 - Buscar o último item da lista
print(films_list[-1])

# 3 - Buscar filmes até uma determinada posição
print(films_list[:3])

# 4 - Buscar filmes de uma posição em diante
print(films_list[1:4])

print()


# Métodos

# 1 - tamanho da lista
print(len(films_list))

# 2 -  retorna a posição do item
print(films_list.index("Sharknado"))

# 3 - Adicionar um item ao final da lista
films_list.append("The Lord of the Rings")
print(films_list)

# 4 - ordena a lista em ordem alfabética
films_list.sort()
print(films_list)

# 5 - Copiar os itens de uma lsita para outra
films_copy = films_list.copy()
films_copy.remove("Sharknado")
print(films_copy)

# 6 - Remove todos os itens da lista
films_list.clear()
print(films_list)

print()

"""
Exercício 1:
Crie uma lista chamada favoritos com 5 filmes que você gosta.
Mostre o primeiro e o último filme
Adicione um novo filme ao final
Ordene a lista em ordem alfabética
Mostre quantos filmes estão na lista
Crie uma cópia da lista chamada top3 apenas com os 3 primeiros
"""

films_list = [
    "Batman Begins",
    "Sharknado",
    "O Menino do Pijama Listrado",
    "O Espetacular Homem Aranha",
    "Procurando Nemo",
]

print(f"{films_list[0]} | {films_list[-1]}")
films_list.append("Carros")
films_list.sort()
"""
Quando usar sort(), saiba que ele altera a lista original. Se quiser preservar a original, use:
lista_ordenada = sorted(minha_lista)

"""
print(len(films_list))
films_list_top3 = films_list[0:3].copy()
print(films_list_top3)

"""
Exercício 2:
Crie uma lista chamada numeros com os valores:
[5, 3, 9, 1, 8]

Ordene a lista
Remova o maior número
Some todos os valores restantes
Mostre a média dos valores (dica: soma / quantidade)
Dica: sum(lista) soma todos os valores da lista
"""

numeros = [5, 3, 9, 1, 8]
numeros.sort()
numeros.remove(numeros[-1])

soma_total = sum(numeros)

media = soma_total / len(numeros)
print("Lista após remoção do maior número:", numeros)
print("Soma total:", soma_total)
print("Média:", media)
