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
        print(f"Avaliação: {self.game_note}\n")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(
            f"Média do jogo {self.game_name}: {self.totalEvaluation / self.evaluators}"
        )
        print(f"Quantidade de avaliações: {self.evaluators}\n")


game1 = Game("Batman: Arkham Knight", 2015, False, 9.0)
game2 = Game("Marvel’s Spider-Man", 2022, False, 10.0)

game1.technical_sheet()
game2.technical_sheet()

game1.evaluate(9.0)
game1.evaluate(7.5)
game1.evaluate(8.5)
game1.evaluate(10.0)
game1.average()

game2.evaluate(9.0)
game2.evaluate(10)
game2.evaluate(9.5)
game2.average()

# Exibindo número total de jogos criados
print(f"Total de jogos criados: {Game.total_games}")
