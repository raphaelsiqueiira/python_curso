"""
Objetivos da aula:
Aprender a usar operadores matemáticos

Compreender operadores lógicos

Usar expressões com comparação
"""

"""
Operadores Matemáticos

| Operador | Significado     | Exemplo   | Resultado |
| -------- | --------------- | --------- | --------- |
|  +       | Adição          |  2 + 3    |  5        |
|  -       | Subtração       |  5 - 2    |  3        |
|  *       | Multiplicação   |  4 * 3    |  12       |
|  /       | Divisão (float) |  10 / 4   |  2.5      |
|  //      | Divisão inteira |  10 // 3  |  3        |
|  %       | Módulo (resto)  |  10 % 3   |  1        |
|  **      | Potência        |  2 ** 3   |  8        |

"""

num1 = 10
num2 = 3

print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Divisão: {num1 / num2}")
print(f"Divisão inteira: {num1 //num2}")
print(f"Resto da divisão: {num1 % num2}")
print(f"Potência: {num1 ** num2}")
print()


"""
Operadores de comparação (Relacionais)
Comparam valores e retornam True ou False:

| Operador | Significado    | Exemplo  |
| -------- | -------------- | -------- |
|  ==      | Igualdade      |  a == b  |
|  !=      | Diferente      |  a != b  |
|  >       | Maior que      |  a > b   |
|  <       | Menor que      |  a < b   |
|  >=      | Maior ou igual |  a >= b  |
|  <=      | Menor ou igual |  a <= b  |

"""

"""
Operadores Lógicos
Combinam condições:

| Operador | Significado   | Exemplo                  |
| -------- | ------------- | ------------------------ |
|  and     | E             |  True and False = False  |
|  or      | Ou            |  True or False = True    |
|  not     | Não (negação) |  not True  False         |
"""

idade = int(input("Digite sua idade:\n"))

maior_de_idade = idade >= 18  # se a idade for maior, ou igual a 18, retorna True

print(f"Você é maior de idade? {maior_de_idade}")
print()


"""
Exercício 1:
Peça dois números ao usuário. Exiba:
A soma
A subtração
A multiplicação
A divisão (com 2 casas decimais)
O resto da divisão
"""

num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))

print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Divisão: {(num1 / num2):.2f}")
print(f"Resto da divisão: {num1 % num2}")

"""
Exercício 2:
Peça a idade do usuário e diga:
Se ele é maior de idade
Se a idade é igual a 18
Se ele é menor que 12 anos
"""

idade = int(input("Digite sua idade:\n"))

print("Você é maior de idade?", idade >= 18)
print("Sua idade é exatamente 18 anos?", idade == 18)
print("Você é menor que 12 anos?", idade < 12)

"""
Exercício 3 (Bônus):
Crie um programa que:
Pergunte se o cliente tem cadastro (responda com “sim” ou “não”)
Pergunte a idade
Mostre se:
Pode acessar o sistema somente se for maior de idade e tiver cadastro


Dica:
Use lower() ao comparar texto do input:
cadastro = input("Tem cadastro? (sim/não):\n").lower()

"""

tem_cadastro = input("Você tem cadastro? (sim/não):\n").lower()
idade = int(input("Digite sua idade:\n"))

acesso_permitido = (tem_cadastro == "sim") and (idade >= 18)

print("Acesso permitido?", acesso_permitido)
