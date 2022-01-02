"""
Player class
"""
import random


class Player:
    """
    Player class with definitios of name, life, and if human or computer
    implements get_roll()
    """

    roll = {"R": 1, "P": 2, "S": 3}

    def __init__(self, name: str, life: int, human: bool = True):
        self.name = name
        self.life = life
        self.human = human

    def get_roll(self) -> int:
        """
        player chooses a play among available options
        :returns
        """
        if self.human:
            play = ""
            option = ["R", "P", "S"]
            while play not in option:
                play = input("Choose wisely: [R]ock - [P]aper - [S]cissor".upper())
                if play not in option:
                    print("Invalid Option")
        else:
            play = random.choice(["R", "P", "S"])
        return Player.roll.get(play, 0)


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

        roll_p1 = self.player1.get_roll()
        roll_p2 = self.player2.get_roll()