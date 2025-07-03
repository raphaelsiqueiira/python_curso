"""
Objetivos desta aula:
Entender como strings funcionam em Python

Conhecer operações básicas (comparação, fatiamento)

Usar métodos úteis de string (como upper(), find(), replace()…)

"""

movie_name = "Top Gun"
movie_name2 = "top Gun"
print(movie_name == movie_name2)
# Python é case sensitive, ou seja, letras maiúsculas são diferentes de minúsculas

movie_description = """
    Top Gun Maverick, é um filme de aviação e aventura,
    muito consagrado na industria
"""

print(movie_name)
print("=" * 30)  # 1 -  Multiplicação de strings
print(movie_description)

# 2 - Procurar uma palavra dentro de um texto
# # O operador "in" verifica se um valor está contido dentro da string.
print("top" in movie_name)
print("Top" in movie_name)

movie_name = "Batman Begins"
# string[inicio:fim] - índice começa na posição 0 | índice final -1

# 3 - Buscar toda string a partir da primeira posição
print(movie_name[0:])
print(movie_name[3:])

# 4 - Buscar toda string até a última posição
print(movie_name[:5])

"""
string[inicio:fim:passo]
índice começa na posição 0 | índice final -1
passo - determina o incremento. Por padrão é o 1
"""
# 5 - Buscar toda a string de 2 em 2 caracteres
print(movie_name[::2])

# 6 - Buscar toda a string nos índices ímpares
print(movie_name[1::2])

# 7 - Inverter uma string de trás para frente
print(movie_name[::-1])


# Metodos

print(movie_name.upper())
print(movie_name)  # Esses métodos retornam novas strings (strings são imutáveis)
print(movie_name.lower())
print(movie_name.capitalize())
print(movie_name.title())
print(
    movie_name.center(20, "-")
)  # Retorna string centralizada com caractere de preenchimento
print(movie_name.find("e"))
print(movie_name.count("a"))
print(movie_name.replace("Batman", "Matrix"))
print(movie_description.split(","))

"""
| Método                         | O que faz                                     |
| ------------------------------ | --------------------------------------------- |
|  .upper()                      | Tudo maiúsculo                                |
|  .lower()                      | Tudo minúsculo                                |
|  .capitalize()                 | Primeira letra maiúscula, resto minúsculo     |
|  .title()                      | Primeira letra de cada palavra maiúscula      |
|  .center(20, "-")              | Centraliza a string com  -  até 20 caracteres |
|  .find("e")                    | Retorna o índice da 1ª ocorrência de "e"      |
|  .count("e")                   | Quantas vezes "e" aparece                     |
|  .replace("Batman", "Matrix")  | Substitui uma palavra por outra               |
|  .split(",")                   | Divide a string onde tiver  ,                 |

"""

"""
Exercício 1:
Crie uma string com o texto:
mensagem = "python é poderoso e divertido"

Mostre a frase toda em maiúsculas
Mostre a frase invertida
Mostre quantas vezes a letra "e" aparece
Mostre apenas a palavra "poderoso" usando fatiamento
"""
mensagem = "python é poderoso e divertido"
print(mensagem.upper())
print(mensagem[::-1])
print(mensagem.lower().count("e"))
print(mensagem[9:17])

"""
Exercício 2:
Peça ao usuário para digitar uma frase e:
Diga se a palavra "python" está na frase (use in)
Mostre a frase com todas as letras maiúsculas
Mostre a quantidade de palavras (use split() + len())
"""
frase = input("Digite uma frase:\n>>>")
print("python" in frase.lower())
print(frase.upper())
print(len(frase.split(" ")))

"""
Exercício 3(Bônus)
Peça ao usuário uma frase e uma palavra.
Depois diga quantas vezes a palavra aparece na frase, independentemente de maiúsculas/minúsculas.
Dica:

frase.lower().count(palavra.lower())
"""
frase = input("Digite uma frase:\n>>>")
palavra = input("Digite uma palavra:\n>>>")
print(frase.lower().count(palavra.lower()))
