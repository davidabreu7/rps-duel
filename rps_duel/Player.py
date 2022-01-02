"""
Player class
"""
import random


class Player:
    """
    Player class with definitios of name, life, and if human or computer
    implements get_roll()
    """

    roll = {0: "Rock", 1: "Paper", 2: "Scissor"}

    def __init__(self, name: str, life: int, human: bool = True):
        self.name = name
        self.life = life
        self.human = human

    def get_roll(self) -> int:
        """
        player chooses a play among available options
        :returns
        """
        option = [0, 1, 2]
        if self.human:
            play = ""
            while play not in option:
                play = int(
                    input(
                        """Choose wisely: 
                0 - Rock 
                1 - Paper 
                2 - Scissor\n"""
                    )
                )
                if play not in option:
                    print("Invalid Option")
        else:
            play = random.choice(option)
        return play


class Match:
    """
    Creates a interaction between Player objects and defines who wins
    """

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def create_match(self):
        """
        make the battle happens: get players rolls and compare with win table
        :return:
        """

        print("---------------------------------------")
        print("        It's time to BATTLE")
        print("---------------------------------------")
        print(f"{self.player1.name} has {self.player1.life} life points")
        print(f"{self.player2.name} has {self.player2.life} life points\n")

        roll_p1 = self.player1.get_roll()
        roll_p2 = self.player2.get_roll()
        winner = (3 + roll_p1 - roll_p2) % 3

        print(f"{self.player1.name} invoked {self.player1.roll.get(roll_p1)}")
        print(f"{self.player2.name} invoked {self.player2.roll.get(roll_p2)}")

        if winner == 1:
            print(f"{self.player1.name} wins!")
            winner = self.player1
            self.player2.life -= 1
        elif winner == 2:
            print(f"{self.player2.name} wins!")
            winner = self.player2
            self.player1.life -= 1
        else:
            print("DRAW")

        return winner
