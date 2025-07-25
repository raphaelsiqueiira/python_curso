"""
O que é um módulo?
Um módulo é um arquivo .py com funções, variáveis ou classes que podem ser importadas e usadas em outros arquivos.

Usamos módulos para:

Reaproveitar código
Organizar funcionalidades por tema
Deixar o código principal mais limpo
"""

# Programa Principal

import math_operation  # Importa o módulo completo
from math_operation import multiply, divide  # Importa funções específicas
import string_utils  # Importa outro módulo


print(string_utils.capitalize("Python"))
print(string_utils.reverse_string("Python"))
print(string_utils.count("Python"))
print()

print(math_operation.sum(5, 3))
print(math_operation.subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 3))
