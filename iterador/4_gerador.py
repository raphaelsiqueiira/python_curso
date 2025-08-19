"""
Yield
> É uma palavra chave para criar geradores. Quando você usa ele em uma função, você transforma a função em um gerador, que é um tipo especial de um iterador.
> Return: Quando executado numa função, é encerrado e o valor é retornado. Chamdas subsequentes à função iniciam a execução novamente do código.
> Yield: Pode ser chamada novamente e retomar a execução do ponto onde foi pausada, permitindo a produção de sequência de valores ao longo do tempo.
"""


def numeros_impares(n):
    for i in range(1, n + 1, 2):
        yield i


for numero in numeros_impares(10):
    print(numero)


def linhas_com_numeros_de_palavras(arquivo, numero):
    with open(arquivo, "r", encoding="utf-8") as file:
        for linha in file:
            if len(linha.split()) == numero:
                yield linha.strip()


arquivo = "texto.txt"
numero_palavras = 3
for linha in linhas_com_numeros_de_palavras(arquivo, numero_palavras):
    print(linha)
