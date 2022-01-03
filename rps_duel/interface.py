
def choose_hand(Player):
    for hand in Player.roll:
        print(f"{hand} - {Player.roll[hand]}")


def start_match(player1, player2):
    print("---------------------------------------")
    print("        It's time to BATTLE")
    print("---------------------------------------")
    print(f"{player1.name} has {player1.life} life points")
    print(f"{player2.name} has {player2.life} life points\n")


def player_hand(player1, player2, rollp1, rollp2):
    print(f"{player1} invoked {rollp1}")
    print(f"{player2} invoked {rollp2}")
