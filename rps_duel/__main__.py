"""
Rock-Paper_Scissor duel game
"""
from Player import Player
from Match import Match


def main():
    humano = Player("Joyce", 3)
    computador = Player("Computador", 3, False)

    partida = Match(humano, computador)
    while humano.life > 0 and computador.life > 0:
        win = partida.create_match()
        if win != 0:
            print(f"{win.name} wins!")
        else:
            print("DRAW")

    print("GAME OVER")


if __name__ == "__main__":
    main()
