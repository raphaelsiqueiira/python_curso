"""
Objetivos

Entender como filtrar elementos de um iterável.

Permitir apenas os elementos que satisfazem uma condição específica.

Aprender a usar filter com funções definidas e lambda.
"""

"""
Filter
- É usada para filtrar elementos de um iterável com base em uma função que pode retornar True ou False.
- Objetivo é permitir apenas os elementos que satisfazem uma condição.
"""


def e_par(x):
    return x % 2 == 0


numeros = [1, 2, 3, 4, 5, 6]

numeros_pares = filter(e_par, numeros)
print(list(numeros_pares))

produtos = [
    {"nome": "Produto A", "preco": 10.0, "em_estoque": True},
    {"nome": "Produto B", "preco": 20.0, "em_estoque": False},
    {"nome": "Produto C", "preco": 30.0, "em_estoque": True},
    {"nome": "Produto D", "preco": 40.0, "em_estoque": False},
]


def produto_em_estoque(produto):
    return produto["em_estoque"]


produtos_disponiveis = filter(produto_em_estoque, produtos)
print(list(produtos_disponiveis))

transacoes = [200.0, -50.0, 75.0, -30.0, 100.0, -10.0]


def e_despesa(transacao):
    return transacao < 0


despesas = filter(e_despesa, transacoes)
print(list(despesas))
