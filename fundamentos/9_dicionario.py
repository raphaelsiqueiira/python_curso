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
print()

idade = int(input("Informe sua idade:\n>>>"))

print(f"Maior de idade? {idade > 18}")
print(f"Você tem 18 anos? {idade == 18}")
print(f"Você tem menos de 12 anos? {idade < 12}")
print()

numero1 = float(input("Digite o primeiro número:\n>>>"))
numero2 = float(input("Digite o segundo número:\n>>>"))

print(
    f"""
O primeiro número é {numero1} e segundo número é {numero2}
Soma: {numero1 + numero2}
Subtração: {numero1 - numero2}
Multiplicação: {numero1 * numero2}
Divisão: {numero1 / numero2}
Resto da divisão: {numero1 % numero2}
"""
)

frase = input("Digite uma frase:\n>>>")
print("python" in frase.lower())
print(frase.upper())
print(len(frase.replace(" ", "")))
print(frase[::-1])

frase = "Python é incrível"
print(frase[frase.find("i") : frase.find("l") + 1])
print(frase.replace("Python", "Programar"))
print()

filmes_favoritos = [
    "Batman Begins",
    "Sharknado",
    "O Menino do Pijama Listrado",
    "O Espetacular Homem Aranha",
    "Procurando Nemo",
]

print(f"Primeiro filme: {filmes_favoritos[0]} | Último filme: {filmes_favoritos[-1]}")
filmes_favoritos.append("Superman")
filmes_favoritos.sort()

filmes_favoritos_copy = filmes_favoritos[0:3].copy()
print(filmes_favoritos_copy)
print()

notas = [7.5, 8.0, 9.2, 6.5, 8.8]

notas.remove(min(notas))
media = sum(notas) / len(notas)
print(media)
print(notas)
print()

dias_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
print(dias_semana[:5])
print(dias_semana[-2:])
print("domingos" in dias_semana)
print(len(dias_semana))
print()

frutas_casa = {"maçã", "laranja", "banana"}
frutas_mercado = {"banana", "uva", "maçã"}

print(f"Ambas: {frutas_casa.intersection(frutas_mercado)}")
print(f"Só em casa: {frutas_casa.difference(frutas_mercado)}")
print(f"Juntas: {frutas_casa.union(frutas_mercado)}")
print()

filme = {
    "titulo": "Batman Begins",
    "ano": 2005,
    "nota": 8.2,
    "genero": ["Superhero", "Action", "Drama"],
}

filme["Diretor"] = "Christopher Nolan"
filme.update({"nota": 9})
filme.pop("genero")
print(filme)
print(filme.keys())
print(filme.values())
print()

filmes_dicionarios = {
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

print(filmes_dicionarios["John Wick"]["director"])

filmes_dicionarios["Batman Begins"]["disponível"] = True
filmes_dicionarios["John Wick"]["avaliable"] = True
del filmes_dicionarios["John Wick"]
print(filmes_dicionarios)
