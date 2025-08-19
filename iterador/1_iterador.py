"""
Objetivos da aula

Entender o que são iteradores.

Aprender como o Python utiliza o protocolo de iteração.

Criar nossa própria classe iteradora com __iter__() e __next__().

Usar o iterador em um for.

------------------------------------

Um iterador é um objeto em Python que permite percorrer uma sequência de valores um por vez, sem precisar armazenar todos na memória de uma só vez.

Ele implementa dois métodos especiais:

__iter__() → retorna o próprio objeto iterador.

__next__() → retorna o próximo valor da sequência.

Quando não há mais elementos, o método __next__() deve levantar a exceção StopIteration, indicando que a iteração terminou.
"""


class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.limite:
            raise StopIteration
        else:
            valor = self.atual
            self.atual += 1
            return valor


contador = Contador(10)
for numero in contador:
    print(numero)

"""
for numero in contador: chama automaticamente o método __iter__().

A cada repetição, o Python chama __next__() para pegar o próximo valor.

Quando o limite é atingido, a exceção StopIteration é levantada, e o laço for termina.
"""

"""
O for em Python internamente chama iter(obj) e depois next(obj).

contador = Contador(5)

iterador = iter(contador)  # Chama __iter__

print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3

Se você continuar chamando next(), ao passar do limite, verá o erro:
StopIteration

"""
