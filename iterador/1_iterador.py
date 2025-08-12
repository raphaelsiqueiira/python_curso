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
