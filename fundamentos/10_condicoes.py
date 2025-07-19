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
print()

"""
Exercício 2: Verificador de número
Peça um número ao usuário e diga se ele é:
Par ou ímpar
Positivo, negativo ou zero
"""

numero = int(input("Digite um número:\n>>>"))

(
    print(f"O número {numero} é par")
    if numero % 2 == 0
    else print(f"O número {numero} é ímpar")
)

if numero > 0:
    print("Ele também é positivo")
elif numero == 0:
    print("O número é zero")
else:
    print("Ele também é negativo")
print()

"""
Exercício 3: Simulador de desconto
Peça o valor de uma compra:
Se for maior que R$ 100, aplicar 10% de desconto
Se for entre R$ 50 e R$ 100, aplicar 5%
Se for menor que R$ 50, não aplicar desconto
"""

valor_compra = float(input("Qual o valor da compra:\n>>>"))
valor_com_desconto = 0

valor_formatado = (
    f"R$ {valor_compra:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)
print(f"Sua compra foi no valor de {valor_formatado}")

if valor_compra > 100:
    valor_com_desconto = valor_compra - (valor_compra * 0.1)
    print(f"Para compras acima de R$ 100,00, você recebe 10% de desconto")

elif valor_compra <= 100 or valor_compra >= 50:
    valor_com_desconto = valor_compra - (valor_compra * 0.05)
    print(
        f"Para compras acima de R$ 50,00 e abaixo de R% 100,00, você recebe 5% de desconto"
    )

else:
    print("Para esse valor, não tem desconto")

valor_com_desconto_formatado = (
    f"R$ {valor_com_desconto:,.2f}".replace(",", "X")
    .replace(".", ",")
    .replace("X", ".")
)

print(f"O valor com desconto é {valor_com_desconto_formatado}")
