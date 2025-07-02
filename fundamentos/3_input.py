"""
Objetivos da aula:
Aprender a capturar dados do usuário com input()

Entender que tudo o que vem de input() é string

Saber converter dados de texto para números com int() e float()

"""

# O que é o input? A função input() permite capturar dados digitados pelo usuário no terminal/console.

name = input("Digite o nome do filme:\n")
year_launch = input("Digite o ano de lançamento do filme:\n")
note_movie = input("Digite a nota do filme:\n")

print(type(name))
print(type(year_launch))
print(type(note_movie))
print()

# O retorno do imput sempre será uma string
# Quando você precisa trabalhar com números, deve converter o que veio do input()
age = int(input("Digite sua idade:\n"))
grade = float(input("Digite sua nota\n"))
print(type(age))
print(type(grade))
print()

"""
Exercício 1:
Crie um programa que:
Pergunte o nome de um produto
Pergunte o preço (float)
Pergunte a quantidade (int)
Calcule e exiba o valor total da compra (preço * quantidade)
Exiba os tipos de cada variável com type()
"""

nome_produto = input("Nome do produto:\n")
preco_produto = float(input("Preço do produto:\n"))
quantidade_produto = int(input("Quantidade do produto:\n"))

valor_compra = preco_produto * quantidade_produto
print(f"Total da compra: {valor_compra:.2f}")

print(type(nome_produto))
print(type(preco_produto))
print(type(quantidade_produto))
print(type(valor_compra))
print()


"""
Exercício 2:
Escreva um programa que:
Peça ao usuário para digitar sua idade
Exiba: "Você tem X anos", onde X é a idade
Mostre se o tipo da variável é realmente inteiro
"""

idade = int(input("Qual sua idade:\n"))
print(f"Você tem {idade} anos")
print(type(idade))
print()
