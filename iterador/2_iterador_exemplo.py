class NomeComLetra:
    def __init__(self, nomes, letra):
        self.nomes = nomes
        self.letra = letra
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.nomes):
            nome = self.nomes[self.index]
            self.index += 1
            if nome.startswith(self.letra):
                return nome
        raise StopIteration


lista_nomes = [
    "Alice",
    "Adrielly",
    "Ana",
    "Bruno",
    "Bruna",
    "Bob",
    "Bart",
    "Carlos",
    "Charles",
    "Damião",
]

letra = "B"

iterador_nomes = NomeComLetra(lista_nomes, letra)

for nome in iterador_nomes:
    print(nome)
