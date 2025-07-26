# Classe pai (Super classe) - Generalista
class Game:
    total_games = 0

    def __init__(self, name="", year_launch=0, multiplayer=False, note=0):
        self.game_name = name
        self.game_year_lauch = year_launch
        self.game_multiplayer = multiplayer
        self.game_note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f"Game: {self.game_name}"

    def technical_sheet(self):
        print()
        print(" DADOS DO JOGO ".center(40, "="))
        print(f"Nome do jogo: {self.game_name}")
        print(f"Ano de lançamento: {self.game_year_lauch}")
        print(f"Multiplayer: {self.game_multiplayer}")
        print(f"Avaliação: {self.game_note}")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(
            f"Média do jogo {self.game_name}: {(self.totalEvaluation / self.evaluators):.2f}"
        )
        print(f"Quantidade de avaliações: {self.evaluators}\n")


# Classe derivada (Subclasse) - Especializada
class SinglePlayerGame(Game):
    def __init__(self, name="", year_launch=0, multiplayer=False, note=0, storyline=""):
        super().__init__(name, year_launch, multiplayer=False, note=note)
        self.game_storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.game_storyline}\n")


mult_game = Game("Call of Duty: Warzone", 2022, True, 5.0)
mult_game.technical_sheet()

mult_game.evaluate(10)
mult_game.evaluate(5)
mult_game.evaluate(7.5)
mult_game.average()
print(f"Total de jogos criados: {Game.total_games}")

sing_game = SinglePlayerGame(
    "Batman: Arkham Knight",
    2015,
    False,
    9.0,
    "História de sobrivivência e vingança",
)
sing_game.technical_sheet()

sing_game.evaluate(9.0)
sing_game.evaluate(7.5)
sing_game.evaluate(8.5)
sing_game.evaluate(10.0)
sing_game.average()
print(f"Total de jogos criados: {Game.total_games}")
