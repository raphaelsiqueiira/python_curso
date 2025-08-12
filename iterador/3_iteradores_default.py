import itertools

# Exemplo 1 - Range()

for i in range(5):
    print(i)

# Exemplo 2  - Iterar Lista

frutas = ["Maça", "Bannaa", "Melão"]
for fruta in frutas:
    print(fruta)

# Exemplo 3 - Iterador Dicionário
pessoa = {"nome": "Alice", "Idade": 30}
for chave in pessoa:
    print(chave, pessoa[chave])

# Exemplo 4 - Enumerate()
frutas = ["Maça", "Bannaa", "Melão"]
for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)

# Exemplo 5 - Zip()

nomes = ["Alice", "Bob", "Carlos"]
idades = [30, 25, 35]
for nome, idade in zip(nomes, idades):
    print(nome, idade)

# Exemplo 6 - Intertools
for i in itertools.count(start=10, step=20):
    if i > 10:
        break
    print(i)
