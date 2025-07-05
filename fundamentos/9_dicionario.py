"""
Objetivos da aula:
Entender o que é um dicionário em Python

Aprender como acessar, adicionar, atualizar e remover itens

Conhecer dicionários aninhados (dentro de dicionários)

Aplicar métodos úteis como keys(), values(), items(), get(), update(), pop(), del
"""

"""
O que é um dicionário?

Dicionários são estruturas de dados do tipo chave:valor.
Ou seja, cada item no dicionário tem uma chave (única) que aponta para um valor.

Sintaxe: 
{
    "chave1": valor1,
    "chave2": valor2,
    ...
}

Geralmente as chaves são str, mas podemos usar qualquer tipo que seja imutável, como:
str, int, float, bool e tuple(se composta só por tipos imutáveis)

Exemplo:
d = {
    42: "idade",
    True: "ativo",
    3.14: "pi",
    (1, 2): "coordenada",
}
"""

film_batman = {
    "title": "Batman Begins",
    "year_release": 2005,
    "imdb_rating": 8.2,
    "genre": ["Superhero", "Action", "Drama"],
}
print(film_batman)
print(type(film_batman))
print(len(film_batman))
print()

# 1 - Recuperar um elemento do dicionário
print(film_batman["genre"])  # Acessa pelo nome da chave
print(film_batman.get("imdb_rating"))
"""
.get acessa de forma segura (não dá erro se não existir)
erro que ocorreria caso não existice:
KeyError: 'nome_da_chave'

Por isso é mais seguro usar get(), que retorna None (ou um valor padrão, se você quiser).

python
Copiar
Editar
print(film.get("diretor"))        # None
print(film.get("diretor", "N/A")) # "N/A" (valor padrão)
"""
print()


# 2 - Buscar apenas as chaves do dicionário
print(film_batman.keys())
print()

# 3 - Buscar apenas os valores do dicionário
print(film_batman.values())
print()

# 4 - Buscar itens do dicinário com chave e valor
print(film_batman.items())
print()

# 5 - Adiciona nova chave e valor no dicionário
film_batman["director"] = "Christopher Nolan"
print(film_batman)
print()

# 6 - Atualizar o valor de uma chave no dicionário
film_batman.update({"imdb_rating": 8.5})
print(film_batman)
print()

# 7 - Remover item do dicionário
film_batman.pop("director")
print(film_batman)
print()

# Dicionários aninhados, ou seja, um dicionário onde os valores também são dicionários

films_dict = {
    "Batman Begins": {
        "year_release": 2005,
        "imdb_rating": 8.2,
        "genre": ["Superhero", "Action", "Drama"],
        "director": "Christopher Nolan",
    },
    "John Wick": {
        "year_release": 2014,
        "imdb_rating": 7.5,
        "genre": ["Action", "Crime", "Gun fu"],
        "director": "Chad Stahelski",
    },
}

print(films_dict)
print(len(films_dict))
print()

# 1 - Buscar uma informação dentro de um dicionário aninhado
print(films_dict["John Wick"]["genre"])
print()

# 2 - Adicionar novo item
films_dict["Batman Begins"]["avaliable"] = True
print(films_dict)
print()

# 3 - Excluir um dicionário
del films_dict["John Wick"]
print(films_dict)
print()

"""
Exercicío 1:
Crie um dicionário com os seguintes dados sobre o filme "Interestelar": (titulo, ano de lançamento, nota e genero)
Mostre apenas a nota do filme
Adicione um novo item: diretor
Atualize a nota para 9.0
Remova o gênero
Crie um dicionário com 2 filmes (aninhado)
Mostre os gêneros do outro filme

"""
film_interestelar = {
    "title": "Interrestellar",
    "year_release": 2014,
    "imdb_rating": 8.6,
    "genre": ["Sci-Fi", "Drama", "Adventure"],
}

print(film_interestelar.get("imdb_rating"))
film_interestelar["director"] = "Christopher Nolan"
film_interestelar["imdb_rating"] = 9.0
film_interestelar.pop("genre")
print(film_interestelar)

films = {
    "Interestelar": film_interestelar,
    "Tenet": {
        "year_release": 2020,
        "imdb_rating": 7.4,
        "genre": ["Sci-Fi", "Action"],
        "director": "Christopher Nolan",
    },
}
print(films)
print(films["Tenet"]["genre"])
