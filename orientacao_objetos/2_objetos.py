class Game:
    name = ""
    year_lauch = 0
    multiplayer = False
    note = 0


# Primeiro Jogo
game1 = Game()
game1.name = "Batman: Arkham Knight"
game1.year_lauch = 2015
game1.multiplayer = False
game1.note = 9.0

# Segundo jogo
game2 = Game()
game2.name = "Marvel’s Spider-Man"
game2.year_lauch = 2022
game2.multiplayer = False
game2.note = 10.0

print(
    f"Nome do jogo: {game1.name} ({game1.year_lauch})\nMultiplayer: {game1.multiplayer}\nNota: {game1.note}"
)
print()
print(
    f"Nome do jogo: {game2.name} ({game2.year_lauch})\nMultiplayer: {game2.multiplayer}\nNota: {game2.note}"
)
