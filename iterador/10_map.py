"""
Map
- Função que aplica uma função a todos os itens de um iteravel(uma lista, por exemplo)
- É uma maneira eficiente e consisa de tranformar dados.
"""

"""
map(func, iteravel) → aplica a função func a cada elemento do iterável.

Vantagem: não precisa criar loops explícitos.

Observação: map retorna um objeto iterável, por isso usamos list() para visualizar todos os resultados de uma vez.
"""


def quadrado(x):
    return x**2


numeros = [1, 2, 3, 4, 5, 6]

for n in numeros:
    print(quadrado(n))

resultado = map(quadrado, numeros)
print(list(resultado))


def celsius_para_fahrenheit(c):
    return (c * 9 / 5) + 32


tempetaturas_celsius = [0, 20, 37, 100]
tempetaturas_fahrenheit = map(celsius_para_fahrenheit, tempetaturas_celsius)
print(list(tempetaturas_fahrenheit))


def normalizar_nome(nome):
    return nome.strip().capitalize()


nomes = "   Ana ", "JOÃO", "maria", "   LUcaS "

nomes_normalizados = map(normalizar_nome, nomes)
print(list(nomes_normalizados))
