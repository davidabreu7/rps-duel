"""
Player class
"""
import random


class Player:
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
            play = input("Choose wisely: [R]ock - [P]aper - [S]cissor".upper())
        else:
            play = random.choice(["R", "P", "S"])
        return Player.roll.get(play, 0)
