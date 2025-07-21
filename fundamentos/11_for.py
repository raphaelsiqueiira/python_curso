films_list = [
    "Batman Begins",
    "Sharknado",
    "O Menino do Pijama Listrado",
    "O Espetacular Homem Aranha",
]

print(films_list)
print()

# 1 - Interando valores de uma lista
for movie in films_list:
    print(movie)
print()

# 2 - Quando a condição for atendida, o loop será encerrado
for movie in films_list:
    print(movie)
    if movie == "O Menino do Pijama Listrado":
        break
print()


# 3 - Quando a condição for atendida, o loop vai para próxima iteração

for movie in films_list:
    if movie == "O Menino do Pijama Listrado":
        continue
    print(movie)
print()

# 4 - Avaliação do filme:

movie_name = input("Digite o nome do filme:\n>>> ")
movie_rating = int(input("Digite quantas avaliações deseja fazer:\n>>> "))

total = 0
for i in range(movie_rating):
    note = float(input(f"Digite a {i+1}º nota para o filme:\n>>> "))
    total += note

if movie_rating > 0:
    average = total / movie_rating
else:
    average = 0

print(
    f"O filme {movie_name} teve {movie_rating} avaliações, com a média de avaliação do filme sendo: {average:.2f}"
)
print()


"""
Exercício
Crie um programa que:

Peça ao usuário para digitar  nomes de filmes favoritos e
armazene os nomes em uma lista.

Use um for para imprimir a lista em ordem numérica:

Exemplo:
1º - Batman
2º - Matrix
...
Depois, pergunte se ele quer remover algum. Se sim, remova usando .remove().

Exiba a nova lista.
"""

quantidade_filmes = int(input("Quantos filmes você quer adicionar a lista:\n>>> "))
lista_filmes = []

for i in range(quantidade_filmes):
    lista_filmes.append(input(f"Digite o nome do {i+1}º filme:\n>>> ").capitalize())
print()

for i in range(len(lista_filmes)):
    print(f"{i+1}º - {lista_filmes[i]}")
print()

quer_remover = input("Você quer remover algum filme?(s/n):\n>>> ").lower()
print()

if quer_remover == "s":
    for i in range(len(lista_filmes)):
        print(f"{i+1}º - {lista_filmes[i]}")
    print()
    remover_filme = int(input("Qual a posição do filme que quer remover:\n>>> "))
    print(f"Você removeu o filme {lista_filmes[remover_filme - 1]} com sucesso.")
    lista_filmes.remove(lista_filmes[remover_filme - 1])
    for i in range(len(lista_filmes)):
        print(f"{i+1}º - {lista_filmes[i]}")
    print()
    print("Fim do programa!")

elif quer_remover == "n":
    print("Você selecionou não. Fim do programa")
else:
    print("Você digitou uma opção inválida. Fim do programa")
