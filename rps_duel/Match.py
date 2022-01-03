from Player import Player
import interface

class Match:
    """
    Creates a interaction between Player objects and defines who wins
    """

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def get_players(self):
        return self.player1, self.player2

    def create_match(self):
        """
        make the battle happens: get players rolls and compare with win table
        :return:
        """

        interface.start_match(self.player1, self.player2)

        roll_p1 = self.player1.get_roll()
        roll_p2 = self.player2.get_roll()
        winner = (roll_p1 - roll_p2) % 7

        interface.player_hand(self.player1.name, self.player2.name, Player.roll.get(roll_p1), Player.roll.get(roll_p2))

        if winner in [4, 5, 6]:
            winner = self.player1
            self.player2.life -= 1
        elif winner in [1, 2, 3]:
            winner = self.player2
            self.player1.life -= 1
        else:
            return 0

        return winner
