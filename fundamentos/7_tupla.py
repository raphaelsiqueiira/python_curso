"""
Objetivos da aula:
Entender o que são tuplas e suas diferenças em relação às listas

Saber acessar elementos com indexação e fatiamento

Utilizar métodos como .index()

Reconhecer quando usar tuplas ao invés de listas

"""

films_tuple = (
    "Batman Begins",
    "Sharknado",
    "O Menino do Pijama Listrado",
    "O Espetacular Homem Aranha",
)
"""
O que é uma tupla?
Uma tupla é imutável: você não pode adicionar, remover ou alterar itens após a criação.

É criada com parênteses () — embora Python aceite também sem parênteses, é boa prática usá-los.

Usada quando você quer garantir integridade dos dados (ex.: coordenadas, configurações fixas, etc.).
"""

print(type(films_tuple))

# 1 - Buscar os dois primieros itens da tupla
print(films_tuple[:2])

# 2 - Buscar o último item da tupla
print(films_tuple[-1])

# 3 - Buscar filmes até uma determinada posição
print(films_tuple[:3])

# 4 - Buscar filmes de uma posição em diante
print(films_tuple[2:])

# 5 - Recuperar um item da tupla pelo nome
print(films_tuple.index("O Espetacular Homem Aranha"))

print("=" * 60)

"""
Tuplas são imutáveis, portanto os métodos que modificam listas(append, sort, remove, etc.) não funcionam com tuplas.
Se tentar usar como exemplo:
films_tuple.append("Matrix")

Vai gerar o erro:
AttributeError: 'tuple' object has no attribute 'append'

"""

"""
Comparação rápida - Lista vs Tupla
| Característica         | Lista                         | Tupla                       |
| ---------------------- | ----------------------------- | --------------------------- |
| Símbolo                |  []                           |  ()                         |
| Mutável?               | Sim                           | Não                         |
| Métodos de modificação | Sim ( append ,  remove , ...) | Não                         |
| Quando usar?           | Dados que mudam               | Dados fixos ou constantes   |

"""

"""
Exercício 1:
Crie uma tupla chamada cidades com 5 cidades.
"São Paulo", "Recife", "Curitiba", "Salvador", "Fortaleza"

Mostre a primeira e a última cidade
Mostre todas menos a primeira
Mostre todas menos a última
Descubra a posição da cidade “Recife”
"""

cidades_tuple = ("São Paulo", "Recife", "Curitiba", "Salvador", "Fortaleza")

print(f"{cidades_tuple[0]} | {cidades_tuple[-1]}")
print(cidades_tuple[1:])
print(cidades_tuple[:-1])
print(cidades_tuple.index("Recife"))
print("=" * 60)
print()

"""
Exercício 2 (Bônus):

dias = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")

Mostre os dias úteis (segunda até sexta)
Mostre os dias do fim de semana (sábado e domingo)
Verifique se "domingo" está na tupla usando in
Mostre o número total de dias na semana (use len())
"""

dias = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")

print(dias[:5])
print(dias[-2:])
print("domingo" in dias)
print(len(dias))
print()

"""
Exercício 3:
Posso colocar uma tupla dentro de outra?
R = Sim, tuplas podem conter outras tuplas. Isso é chamado de tupla aninhada (nested tuple).
Uma tupla é uma coleção de elementos imutáveis.
Mas esses elementos podem ser de qualquer tipo, inclusive outras tuplas.

Exemplo:
"""
filmes_fixos = (
    ("Batman Begins", 2005, 8.2),
    ("Matrix", 1999, 8.7),
    ("Interestelar", 2014, 8.6),
)
print(filmes_fixos)

# Acessando a tupla completa do primeiro filme
print(filmes_fixos[0])

# Acessando o nome do segundo filme
print(filmes_fixos[1][0])

# Acessando o ano do terceiro filme
print(filmes_fixos[2][1])
