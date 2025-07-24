# 1 - Fatorial de um número


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


number = int(input("Digite o número para o fatorial:\n>>> "))
print(f"O fatorial de {number} é {factorial(number)}")
print()


def total_sum(num):
    if num == 1:
        return 1
    else:
        return num + total_sum(num - 1)


num = int(input("Digite o número para soma:\n>>> "))
print(f"A soma total {num} é {total_sum(num)}")
print()


"""
Exercício proposto:
Crie uma função recursiva chamada countdown(n) que conte de n até 0 e imprima:
3...
2...
1...
0!
"""


def countdown(n):
    if n == 0:
        print("0!")
    else:
        print(f"{n}...")
        countdown(n - 1)


print()

valor = int(input("Digite o valor para o contador:\n>>> "))
countdown(valor)
