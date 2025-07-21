films_list = [
    "Batman Begins",
    "Sharknado",
    "O Menino do Pijama Listrado",
    "O Espetacular Homem Aranha",
]

print(films_list)
print()

# 1 - Iterando valores de uma lista de filmes usando while
index = 0
while index < len(films_list):
    print(films_list[index])
    index += 1
print()

# 2 - Quando a condição for atendida o loop será encerrado
index = 0
while index < len(films_list):
    print(films_list[index])
    if films_list[index] == "O Menino do Pijama Listrado":
        break
    index += 1
print()

# 3 - Quando a condição for atendida o loop vai para a próxima iteração
index = 0
while index < len(films_list):
    if films_list[index] == "O Menino do Pijama Listrado":
        index += 1
        continue
    print(films_list[index])
    index += 1
print()

# 4 - Avaliação do filme com while
movie_name = input("Digite o nome do filme:\n>>> ")
movie_rating = int(input("Digite quantas avaliações deseja fazer:\n>>> "))

total = 0
count = 0

while count < movie_rating:
    note = float(input(f"Digite a {count+1}º nota para o filme:\n>>> "))
    total += note
    count += 1

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
Crie um sistema que peça o nome de vários filmes (um por vez) e adicione em uma lista até o usuário digitar "sair".
Ao final, mostre todos os filmes digitados em ordem.
"""
lista_filmes = []
while True:
    nome_filme = input(
        'Digite o nome de um filme para adicionar a lista(digite "sair" para parar o programa)\n>>> '
    ).lower()

    if nome_filme == "sair":
        print("Você digitou sair. Fim do programa")
        print()
        if len(lista_filmes) > 0:
            print("Veja abaixo a lista de filmes que você adicionou")
            for i, filme in enumerate(lista_filmes, start=1):
                print(f"{i}º - {filme}")
        break
    elif nome_filme == " " or nome_filme == "":
        print()

        print("Opção inválida. Tente novamente")
    else:
        print()
        lista_filmes.append(nome_filme.capitalize())
        for i, filme in enumerate(lista_filmes, start=1):
            print(f"{i}º - {filme}")
