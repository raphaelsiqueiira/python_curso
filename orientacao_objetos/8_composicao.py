"""
O que é Programação Orientada a Objetos?
POO é um paradigma que organiza o código em torno de objetos, que representam entidades do mundo real com características (atributos) e comportamentos (métodos).

Exemplo: Um “jogo” tem nome, nota, se é multiplayer ou não, e pode ser avaliado.
"""


class Game:
    # 	Método especial chamado automaticamente ao criar o objeto
    def __init__(self, name="", year_launch=0, multiplayer=False, note=0):
        self.game_name = name
        self.game_year_lauch = year_launch
        self.game_multiplayer = multiplayer
        self.game_note = note
        self.totalEvaluation = 0
        self.evaluators = 0

    # Self representa a instância atual da classe

    def __str__(self):
        return f"Game: {self.game_name}"

    # Retorna uma representação textual do objeto, útil para print(game1)

    def technical_sheet(self):
        print()
        print(" DADOS DO JOGO ".center(40, "="))
        print(f"Nome do jogo: {self.game_name}")
        print(f"Ano de lançamento: {self.game_year_lauch}")
        print(f"Multiplayer: {self.game_multiplayer}")
        print(f"Avaliação: {self.game_note}\n")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
        average_grades = self.totalEvaluation / self.evaluators
        self.game_note = average_grades

    def average(self):
        print(f"Média do jogo {self.game_note}")
        print(f"Quantidade de avaliações: {self.evaluators}\n")


class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.game_note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estúdio {self.name} ainda não lançou nenhum jogo")
        else:
            average_note = total_notes / num_games
            print(
                f"Avaliação média dos jogos do estúdio {self.name}: {average_note:.2f}"
            )


game1 = Game("Batman: Arkham Knight", 2015, False, 9.0)
game2 = Game("Marvel’s Spider-Man", 2022, False, 10.0)

studio = GameStudio("Awesome Game")


game1.evaluate(9.0)
game1.evaluate(7.5)
game1.average()

game2.evaluate(9.0)
game2.evaluate(10)
game2.average()

studio.add_game(game1)
studio.add_game(game2)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()
