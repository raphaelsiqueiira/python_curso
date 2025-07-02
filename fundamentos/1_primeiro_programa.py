"""
Objetivos da aula:
Entender como funciona a execução de um código Python

Compreender o uso de comentários

Utilizar a função print()

Conhecer boas práticas básicas
"""

# Isso é um comentário de uma linha
# Comentários não são executados. Eles servem para explicar o código.

"""
Python não possui um comentário de múltiplas linhas oficial como /**/ em outras linguagens. Mas existe uma prática comum adicionando
três aspas simples ou duplas.
Apesar de parecer um comentário, tecnicamente isso é uma docstring não atribuída.
Docstrings são strings de documentação usadas para explicar o que um pedaço de código faz. 
"""

# A função print() serve para exibir mensagens na tela. É o nosso primeiro contato com saída de dados.

print("Olá Mundo")
print("Aprendendo a Linguagem Python\n")

# A função print() envia esse texto para a saída padrão (geralmente o console ou terminal).

"""
Boas práticas:
1 - Use comentários claros e úteis.
Não escreva obviedades, ou tente consertar um código ruim explicando o que ele faz

2 - Use nomes de arquivos significativos.
Evite nomes como script1.py, arquivo.py

3 - Organize visualmente seu código. 
Use quebras de linha para separar blocos de código por ideia.

4 - PEP 8.
PEP 8 (Python Enhancement Proposal 8) é um documento que estabelece as diretrizes para a escrita de código Python. Essas diretrizes visam tornar o código mais fácil de ler, entender e manter, tanto para o autor quanto para outros desenvolvedores
"""

"""
Exercícios:

1 - Imprima três mensagens diferentes, por exemplo
Bom dia!
Estou aprendendo Python
Esse é o meu primeiro programa
"""

print("Bom dia!")
print("Estou aprendendo Python")
print("Esse é o meu primeiro programa")

"""
2 - Explique com suas palavras o que o código abaixo faz:
print("Programar é transformar ideias em realidade!")
"""

# O código exibe uma mensagem na tela. Ele imprime o texto passado como argumento para a função print()

"""
3 - Bônus:
Imprima a seguinte saída respeitando as quebras de linha:
Bom dia!
Estou aprendendo Python
Esse é o meu segundo programa
"""

print(
    """
Bom dia
Estou aprendendo Python
Esse é o meu segundo programa
"""
)

print("Bom dia!\nEstou aprendendo Python\nEsse é o meu segundo programa")
