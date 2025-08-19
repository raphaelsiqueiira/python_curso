"""
Nesta aula, vamos explorar como o Python já nos fornece formas práticas de iterar coleções e também como a biblioteca itertools pode nos ajudar a criar iteradores infinitos ou controlados.

Você já viu como criar iteradores manuais (__iter__ e __next__), mas na maioria das vezes, o Python oferece soluções mais simples e diretas.
"""

import itertools

# Exemplo 1 - Range()
# O range() é um iterador que gera números em sequência dentro de um intervalo.

for i in range(5):
    print(i)

# Exemplo 2  - Iterar Lista
# Qualquer lista em Python é iterável

frutas = ["Maça", "Bannaa", "Melão"]
for fruta in frutas:
    print(fruta)

# Exemplo 3 - Iterador Dicionário
# Dicionários também são iteráveis.
# Se iterarmos diretamente sobre eles, recebemos as chaves.
pessoa = {"nome": "Alice", "Idade": 30}
for chave in pessoa:
    print(chave, pessoa[chave])

# Exemplo 4 - Enumerate()
# O enumerate() é útil para obter tanto o índice quanto o valor de uma lista.
frutas = ["Maça", "Bannaa", "Melão"]
for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)

# Exemplo 5 - Zip()
# O zip() combina elementos de duas (ou mais) listas em pares.
# Se as listas tiverem tamanhos diferentes, o zip para no final da menor.

nomes = ["Alice", "Bob", "Carlos"]
idades = [30, 25, 35]
for nome, idade in zip(nomes, idades):
    print(nome, idade)

# Exemplo 6 - Intertools
# O módulo itertools traz funções poderosas para trabalhar com iteradores.
# Um exemplo é count(), que gera números infinitos em uma progressão aritmética.

for i in itertools.count(start=0, step=2):
    if i > 10:
        break
    print(i)
