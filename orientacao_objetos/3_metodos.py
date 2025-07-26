class Game:
    def __init__(self, name="", year_launch=0, multiplayer=0, note=0):
        self.game_name = name
        self.game_year_lauch = year_launch
        self.game_multiplayer = multiplayer
        self.game_note = note

    def __str__(self):
        return f"Game: {self.game_name}"


game1 = Game("Batman: Arkham Knight", 2015, False, 9.0)
game2 = Game("Marvel’s Spider-Man", 2022, False, 10.0)
print(game1)
print()
print(
    f"{game1.game_name} - ({game1.game_year_lauch})\nMultiplayer: {game1.game_multiplayer}\nAvaliação: {game1.game_note}"
)
print()

print(
    f"Nome do jogo: {game2.game_name} ({game2.game_year_lauch})\nMultiplayer: {game2.game_multiplayer}\nNota: {game2.game_note}"
)
