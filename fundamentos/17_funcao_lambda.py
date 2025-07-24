"""
O que é uma função lambda?
Em Python, uma função lambda é uma forma enxuta de criar funções simples, geralmente em uma única linha.
"""

# Função de potência de um número

power = lambda num: num**2
print(power(5))
print(power(10))
print()

# Função que verifica se o número é par ou ímpar
is_even = lambda x: x % 2 == 0

print(is_even(7))
print(is_even(10))
print()

# Função que divide um número por outro
div_num = lambda num1, num2: num1 / num2

print(div_num(10, 2))
print(div_num(25, 5))

# Função que divide uma string
reverse_string = lambda s: s[::-1]

print(reverse_string("Python"))
print(reverse_string("Batman"))
print()

# Funcionalidades relacionadas aos filmes:
films_list = [
    "Batman Begins",
    "Sharknado",
    "O Menino do Pijama Listrado",
    "O Espetacular Homem Aranha",
    "Procurando Nemo",
]
ratings = {
    "Batman Begins": [10, 9, 8.5, 8.5],
    "Sharknado": [10, 7, 8.5, 6.5],
    "O Menino do Pijama Listrado": [10, 9, 8.5, 9.5],
    "O Espetacular Homem Aranha": [10, 9, 7, 8.5],
    "Procurando Nemo": [10, 9, 7.5, 8.5],
}

# Função para calcular a média de avaliações de um filme
average_rating = lambda movie_name: sum(ratings[movie_name]) / (
    len(ratings[movie_name])
)

for film in films_list:
    print(f"Média de Avaliação do filme: {film} - {average_rating(film)}")

# Função verifica se um filme está na lista
check_movie = lambda movie_name: movie_name in films_list

print(f"Fuga das galinhas está na lista? {check_movie('Fuga das Galinhas')}")


# Recomenda um filme com base na avaliação média

recommend_movie = (
    lambda movie_name: f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):.2f}"
)


print(recommend_movie("Batman Begins"))

"""
| Use quando...                              | Evite quando...                            |
| ------------------------------------------ | ------------------------------------------ |
| A função for curta (1 linha)               | A função for complexa ou com muitas regras |
| Você quer passar uma função como argumento | Precisa de vários passos ou condições      |
| Quer melhorar legibilidade pontual         | Vai reutilizar o código várias vezes       |

"""
