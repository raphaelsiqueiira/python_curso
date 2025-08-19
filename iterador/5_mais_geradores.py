# 1 - Gerador de expressão
quadrados = (x**2 for x in range(10))
for quadrado in quadrados:
    print(quadrado)


# 2 Iterador Infinito
def contador_infinito():
    i = 0
    while True:
        yield i
        i += 1


contador = contador_infinito()
for _ in range(10):
    print(next(contador))


# 3 - Coleta de valores com send()
def gerador_soma():
    total = 0
    while True:
        valor = yield total
        if valor is not None:
            total += valor


soma = gerador_soma()
next(soma)

print(soma.send(10))
print(soma.send(5))
print(soma.send(15))


# 4 - Tratamento de Exceções
def gerador_excecao():
    try:
        while True:
            valor = yield
            print(f"Valor recebido: {valor}")
    except ValueError:
        print("Valor inválido!")


g = gerador_excecao()
next(g)
g.send(10)
# g.throw(ValueError)


# 5 - Cascata de geradores
def multiplicar_por_dois(iterable):
    for i in iterable:
        yield i * 2


def adicionar_cinco(iterable):
    for i in iterable:
        yield i + 5


numeros = range(5)
resultado = adicionar_cinco(multiplicar_por_dois(numeros))
for r in resultado:
    print(r)
