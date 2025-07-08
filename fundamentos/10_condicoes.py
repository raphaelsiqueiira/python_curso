"""
 Objetivos da Aula
Aprender a usar estruturas condicionais em Python.

Compreender o uso de if, elif e else para tomar decisões no código.

Criar programas interativos baseados em entradas do usuário.

"""

"""
O que é uma estrutura condicional?
Em Python (e em qualquer linguagem de programação), estruturas condicionais permitem tomar decisões com base em uma condição lógica.

if condição:
    # código se a condição for verdadeira
elif outra_condição:
    # código se a primeira for falsa e essa for verdadeira
else:
    # código se nenhuma das anteriores for verdadeira


Importante:
Os blocos em Python usam indentação (geralmente 4 espaços ou 1 Tab).
O elif é opcional e pode ser usado várias vezes.
O else também é opcional, mas só pode aparecer uma vez e sempre por último.
"""

# Informações sobre o filme
name = input("Digite o nome do filme:\n>>>")
rating = float(input("Digite a nota de avaliação do filme:\n>>>"))

# Verifica se o filme é recomendado
if rating > 8.0:
    print(f"O filme {name} é muito bom. Recomendo assísti-lo.")
else:
    print(f"O filme {name} ainda não atingiu uma boa nota.")
print()

num1 = float(input("Digite o primeiro número:\n>>> "))
num2 = float(input("Digite o segundo número:\n>>> "))
operation = input("Digite a operação a ser realizada: (+ - * /)\n>>> ")

result = 0
mensagem_error = False

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        mensagem_error = True
else:
    print("Operação inválida")
    result = 0

if operation == "/" and mensagem_error:
    print("Erro: Divisão por zero.")
else:
    print(f"Resultado da operação é {result:.2f}")
print()

"""
Cuidados comuns de quem está aprendendo:
Esquecer dos dois pontos (:) no final do if, elif ou else

Não indentar o código dentro dos blocos

Usar = (atribuição) em vez de == (comparação)
"""

"""
Exercício 1:
Faça um programa que pergunte a idade do usuário e diga:

Se é menor de idade (menor que 18)
Se tem 18 anos exatos
Se é maior de idade (maior que 18)
"""
idade = int(input("Qual sua idade:\n>>>"))

if idade < 18:
    print("Você é menor de idade!")
elif idade == 18:
    print("Você tem 18 anos")
else:
    print("Você tem mais de 18 anos")
