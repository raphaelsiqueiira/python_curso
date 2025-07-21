# 1 - Listando valores de 0 a 10 que sejam menos do que 4
for i in range(10):
    if i < 4:
        print(i)
print()

# 2 - Com list comprehession
list_numbers = [i for i in range(10) if i < 4]
print(list_numbers)
print()


# 3 - Filmes que possuem a letra "e" no título
films_list = [
    "Batman Begins",
    "Sharknado",
    "O Menino do Pijama Listrado",
    "O Espetacular Homem Aranha",
]

movie_with_e = [movie for movie in films_list if "e" in movie.lower()]
print(movie_with_e)
print()

movies_watched = [movie for movie in films_list if movie != "Sharknado"]
print(movies_watched)
print()


while True:
    nome_filme = input(
        'Digite o nome de um filme para procurar na lista(digite "sair" para parar o programa)\n>>> '
    ).lower()

    if nome_filme == "sair":
        print("Você digitou sair. Fim do programa")
        print()
        if len(films_list) > 0:
            print("Veja abaixo a lista de filmes que você adicionou")
            for i, filme in enumerate(films_list, start=1):
                print(f"{i}º - {filme}")
        break
    elif nome_filme == " " or nome_filme == "":
        print()

        print("Opção inválida. Tente novamente")
    found_movies = [
        movie for movie in films_list if nome_filme.lower() in movie.lower()
    ]
    if found_movies:
        print(f"Filme(s) encontrados com o nome {nome_filme}:")
        for found_movie in found_movies:
            print(f"{films_list.index(found_movie) + 1} - {found_movie}")
        print()
    else:
        print(f"Nenhum filme foi encontrado com o nome {nome_filme}. Tente novamente")
        print()
