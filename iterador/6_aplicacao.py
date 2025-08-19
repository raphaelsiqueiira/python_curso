class VendasIterador:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.file = open(arquivo, "r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self):
        linha = self.file.readline()
        if not linha:
            self.file.close()
            raise StopIteration
        categoria, valor = linha.strip().split(",")
        return categoria, float(valor)


def gerador_soma_vendas(arquivo):
    total_vendas = 0
    for categoria, valor in VendasIterador(arquivo):
        total_vendas += valor
        yield categoria, valor, total_vendas


contagem_vendas = {}
arquivo = "vendas.txt"
print("Processando Vendas...")
for categoria, valor, total in gerador_soma_vendas(arquivo):
    print(f"Categoria: {categoria}, Valor R$: {valor:.2f}, Total R$: {total:.2f}")

    if categoria not in contagem_vendas:
        contagem_vendas[categoria] = 0
    contagem_vendas[categoria] += 1

for categoria, contagem in contagem_vendas.items():
    print(f"{categoria}: {contagem} vendas")
