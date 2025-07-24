"""
O que é *args?
É utilizado quando queremos passar uma quantidade indefinida de argumentos posicionais

Eles chegam na função como uma tupla
"""


# 1 - Soma de números
def soma(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")


soma(7)
soma(7, 9)
soma(7, 9, 10, 11)

"""
O que é **kwargs?
Serve para passar um número indefinido de argumentos nomeados (com chave e valor).

Esses dados são recebidos como um dicionário.
"""


# 2 - Apresentação de Filmes
def presentation_movies(**data):
    for key, value in data.items():
        print(f"{key} - {value}")


print()
print("Lista de Cursos:")
print()

presentation_movies(name="Batman", year_launch=2005, note_movie=9.5, available=True)
print()
presentation_movies(name="Matrix", note_movie=8.5, available=True)
print()

presentation_movies(name="Carros")
print()


def avaliar_filme(nome_filme, *notas, **informacoes):
    print(f"\nFilme: {nome_filme}")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Notas recebidas: {notas}")
        print(f"Média das avaliações: {media:.2f}")
    else:
        print("Nenhuma nota foi fornecida.")

    if informacoes:
        print("\n Informações Adicionais:")
        for chave, valor in informacoes.items():
            print(f"- {chave.capitalize()}: {valor}")
    else:
        print("\nNenhuma informação extra fornecida")


avaliar_filme(
    "Interestelar",
    8.5,
    9.0,
    10,
    ano=2014,
    diretor="Christopher Nolan",
    genero="Ficção científica",
)


avaliar_filme("Sharknado", 2, 3, ano=2013, diretor="Anthony C. Ferrante")

avaliar_filme("Matrix")
