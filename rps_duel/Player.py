"""
Player class
"""
import random

import interface


class Player:
    """
    Player class with definitios of name, life, and if human or computer
    implements get_roll()
    """

    moves = ["Rock", "Fire", "Scissor", "Sponge", "Paper", "Air", "Water"]
    roll = {index: move for index, move in enumerate(moves)}

    def __init__(self, name: str, life: int, human: bool = True):
        self.name = name
        self.life = life
        self.human = human

    def get_roll(self) -> int:
        """
        player chooses a play among available options
        :returns
        """
        option = range(0, 7)
        if self.human:
            play = ""
            while play not in option:
                interface.choose_hand(Player)
                play = int(input("Choose your hand:"))
                if play not in option:
                    print("Invalid Option")
        else:
            play = random.choice(option)
        return play
