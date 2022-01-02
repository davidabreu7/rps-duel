"""
Rock-Paper_Scissor duel game
"""
from Player import Player, Match


def main():
    humano = Player("Joyce", 3)
    computador = Player("Computador", 3, False)

    partida = Match(humano, computador)
    while humano.life > 0 and computador.life > 0:
        partida.create_match()
        print(partida.player1.life)

    print("GAME OVER")


if __name__ == "__main__":
    main()
