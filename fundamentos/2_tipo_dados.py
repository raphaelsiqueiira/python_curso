"""
Objetivos da aula:
Compreender o conceito de variável e constante

Conhecer os tipos de dados primitivos: str, int, float, bool

Usar a função type() para identificar tipos

Escrever boas práticas no uso de nomes

Criar saídas com print() usando concatenação, format() e f-strings

"""

"""
 O que é uma variável?
 Uma variável é como uma caixa com um nome, que armazena algum dado na memória.
 O valor dentro da variável pode mudar durante o programa. Por isso o nome variável

 Exemplo:
 name = "Fulano"

 name é o identificador da variável (nome escolhido)
 "Fulano" é o valor armazenado na variável
"""

"""
O que é uma constante?
Diferente das variáveis, as constantes não devem mudar seu valor durante o programa.
Python não possui constantes de forma nativa como outras linguagens, mas usamos uma convenção:
Toda constante deve ser escrita com letras maiúsculas e separada por _ (snake case):

Exemplo:
TAXA_JUROS = 0.13
PI = 3.14159

Importante: Python permite mudar o valor de uma "constante", mas não devemos fazer isso, por convenção.
"""

"""
Tipos de dados      | Explicação                                     | Exemplo
-----------------------------------------------------------------------------------
1 - str (String)     | Texto entre aspas simples ou duplas           | "Fulano", 'Ciclano', "22"
2 - int (Inteiro)    | Números inteiros, sem vírgula                 | 5, 2025, 14
3 - float (Decimal)  | Números com ponto decimal (ponto,não vírgula) | 5.2, 10.4, 3642.8
4 - bool (Booleano)  | Lógicos: True ou False (1º letra maiúscula)   | True, False


"""

# Locadora de Filmes

movie_name = "Batman Begins"  # string
year_launch = 2005  # int
note_movie = 8.2  # float
available = True  # bool

print(
    "Nome do Filme: " + movie_name
)  # caso o valor da variável fosse um número, daria erro pois ele tentaria somar um texto com um número
print(type(movie_name))
print()

print(
    "Data de lançamento: {}".format(year_launch)
)  # ainda é amplamente utilizado, embora o f-string seja mais moderno e recomendado desde o Python 3+
print(type(year_launch))
print()

print(f"Nota do Filme: {note_movie}")  # recomendado
print(type(note_movie))
print()

print("Disponível para locação:",available)
print(type(available))
print()


"""
Boas práticas:
1 - Use nomes significativos:
note_movie é mais legível que notemovie

2 - Evite usar nome com acentos ou espaços

3 - Python comumente segue a convenção snake_case:
A convenção snake_case recomenda que nomes de variáveis sejam escritos em letras minúsculas, com palavras separadas por underscores (_).
Ao invés de colocar a letra da próxima palavra como maiúscula, como o caso da convenção camelCase

"""

"""
Exercícios: 

1 - Explique com suas palavras a diferença entre os tipos: str, int, float e bool:

Resposta = O tipo str representa textos (sequência de caracteres), o tipo int representa números inteiros, float representa números decimais com ponto, e bool representa valores lógicos: verdadeiro ou falso (True ou False)
"""

"""
2 - Escreva um código que exiba o seguinte diálogo, usando variáveis:
O filme escolhido foi: Matrix
Lançado em: 1999
Nota: 8.7
Disponível? True
"""

nome_filme = "Matrix"
ano_lancamento = 1999
nota_filme = 8.7
disponibilidade = True

print(f"O filme escolhido foi: {nome_filme}")
print(f"Lançado em: {ano_lancamento}")
print(f"Nota: {nota_filme}")
print(f"Disponível? {disponibilidade}")

"""
3 - Bônus: 
Armazene um filme com nome (str), ano (int), nota (float) e se está disponível (bool).
Depois exiba as informações no seguinte formato: 

Filme 1: Interstellar (2014) - Nota: 8.6 - Disponível? True  
"""
nome_filme = "Interstellar"
ano_lancamento = 2014
nota_filme = 8.6
disponibilidade = True

print(
    f"Filme 1: {nome_filme } ({ano_lancamento}) - Nota: {nota_filme} - Disponível? {disponibilidade}"
)


# Dica: Você pode formatar um número com casas decimais específicas usando:
print(f"Nota: {nota_filme:.2f}")  # Mostra 8.6 com 2 casas decimais
