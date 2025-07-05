"""
Objetivos da aula:
Entender o que é um set (conjunto) em Python

Conhecer suas características principais

Usar métodos úteis como len(), update() e remove()

Comparar set com listas e tuplas
"""

"""
O que é um set?
Um set (conjunto) é uma estrutura de dados não ordenada, imutável em termos de posição 
(significa que você não consegue acessar ou mudar um valor pela posição (índice) e que não permite elementos duplicados).

Usado com chaves {}
Ideal para armazenar elementos únicos
Não preserva ordem
Não permite acesso por índice ou fatiamento
"""

films_set = {
    "Batman Begins",
    "Sharknado",
    "O Menino do Pijama Listrado",
    "O Espetacular Homem Aranha",
}

print(type(films_set))
print()

# 1 - Buscar o tamanho do set
print(len(films_set))
print()

# 2 - True e 1 são considerados o mesmo valor em um set porque ambos são tratados como o número 1 internamente
example_set = {"Matrix", True, 1, 8.7}
print(example_set)
print()

# 3 - Adicionar item de outro set
films_set.update(example_set)
print(films_set)
print()

# 4 - Remover um item do set
films_set.remove(True)
films_set.remove(8.7)
print(films_set)
print()

"""
| Característica    | Lista[]                   | Tupla()               | Set{}                       |
| ----------------- | ------------------------- | --------------------- | --------------------------- |
| Ordenada          |   Sim                     |   Sim                 |   Não                       |
| Permite repetição |   Sim                     |   Sim                 |   Não                       |
| Acessa por índice |   Sim                     |   Sim                 |   Não                       |
| Mutável           |   Sim                     |   Não                 |   Sim (mas sem ordem)       |
| Uso comum         | Dados variados, que mudam | Dados fixos e seguros | Conjuntos únicos, sem ordem |

"""

"""
Exercício 1 (Difícil - Bônus):
Crie um set chamado frutas com 4 frutas.
Depois:

Mostre o número de frutas
Tente adicionar uma fruta repetida
Mostre o set e veja se ele aceitou a duplicata
Remova uma fruta
Adicione mais 2 frutas com update()

A função set.update() espera um objeto iterável — como uma lista, outro set, ou qualquer coleção de múltiplos elementos.
"""

frutas = {"banana", "maçã", "pêra", "abacaxi"}
print(frutas)

print(len(frutas))
frutas.add(
    "banana"
)  # use add para adicionar apenas um item específico (string completa)
print(frutas)
frutas.discard("abacaxi")
frutas.update(["morango", "uva"])  # Adiciona as palavras inteiras
print(frutas)
print()

"""
Exercício 2:
Crie dois sets: 
frutas_mercado = {"banana", "maçã", "uva"}
frutas_casa = {"maçã", "laranja", "pera"}

1 - Mostre as frutas que estão em ambos os sets (interseção)
2 - Mostre as frutas que estão no mercado, mas não em casa (diferença)
3 - Mostre todas as frutas (união)

Dica: Use métodos set.intersection(), set.difference(), set.union()

Explicação dos métodos:

1 - intersection(): Retorna um novo set com os elementos que existem em ambos os sets (interseção).
   Ou seja, as frutas que estão presentes tanto no mercado quanto em casa.

2 - difference(): Retorna um novo set com os elementos que estão no primeiro set, mas não no segundo.
   Ou seja, as frutas que você encontra no mercado, mas que não tem em casa.

3 - union(): Retorna um novo set com todos os elementos de ambos os sets, sem repetição.
   Ou seja, todas as frutas que estão no mercado ou em casa (união dos dois sets).

   estrutura de exemplo:
   primeiro_set.metodo(segundo_set)
"""

frutas_mercado = {"banana", "maçã", "uva"}
frutas_casa = {"maçã", "laranja", "pera"}

print("Frutas em ambos os lugares:", frutas_mercado.intersection(frutas_casa))
print("Frutas só no mercado:", frutas_mercado.difference(frutas_casa))
print("Todas as frutas:", frutas_mercado.union(frutas_casa))


"""
Complementos e explicações
- Set não tem ordem e é mutável — o que isso significa na prática?
    - Você pode adicionar ou remover elementos (mutável).
    - Mas não pode acessar elementos por índice porque a ordem dos elementos é imprevisível e muda a qualquer operação.
    - Isso é diferente de listas e tuplas, que são ordenadas e você pode acessar elementos pelo índice.

- Por que True e 1 são considerados iguais no set?
    - Em Python, True é um subtipo de int e seu valor numérico é 1.
    - Como sets armazenam apenas valores únicos, True e 1 são tratados como o mesmo elemento.

- Métodos úteis para sets
    - add() — adiciona um único item.
    - update() — adiciona vários itens de uma vez, recebendo qualquer iterável (lista, tupla, outro set).
    - remove() — remove um item específico (causa erro se o item não existir).
    - discard() — remove um item, mas não causa erro se o item não existir (mais seguro).
"""
