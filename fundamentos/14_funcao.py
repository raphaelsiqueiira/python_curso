# 1 - Função para imprimir uma mensagem
"""
def welcome():
    print("Bem vindo ao sistema de filmes!")


welcome()
# 2 - Função para calcular a média de notas


def calculate_average():
    num_ratings = int(
        input("Digite quantas avaliações deseja fazer para o filme:\n>>> ")
    )
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme:\n>>> "))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    return average


print(f"A média de avaliações do filme foi {calculate_average():.2f}")
"""
# 3 - Função para cadastrar um filme:
list_films = []


def create_movie():
    name = input("Digite o nome do filme:\n>>> ")
    year_launch = int(input("Digite o ano de lançamento do filme:\n>>> "))
    note_movie = float(input("Digite a nota do filme:\n>>> "))
    movie_price = float(input("Digite o preço do filme:\n>>> "))

    movie = {
        "title": name,
        "year_release": year_launch,
        "imdb_rating": note_movie,
        "price": movie_price,
    }

    list_films.append(movie)
    return list_films


"""
for i, filme in enumerate(list_films, start=1):
    print(f"{i}º - {filme}")
"""

# Usando argumentos nas funções


# 1 - Função para imprimir um nome commpleto
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


print(full_name("Fulano", "De Tal"))
print(f"O nome completo é: {full_name("João", "Feijão")}")
print()


# 2 - Função para somar dois números
def sum_number(a, b):
    return a + b


print(f"Soma é: {sum_number(100, 50)}")
print()


# 3 - Função com parâmetro default
def sum_number_default(a=0, b=0):
    return a + b


print(f"Soma é: {sum_number_default(30, 25)}")
print(f"Soma é: {sum_number_default()}")
print()


# 4 - Função para criar filme


def list_all_movies(list_films=list_films):
    for i, filme in enumerate(list_films, start=1):
        print(f"{i}º - {filme}")


def create_movies(number_of_movies=0):
    for movie in range(number_of_movies):
        create_movie()
    list_all_movies()


number_of_movies = int(input("Quantos filmes deseja criar? "))
create_movies(number_of_movies)
