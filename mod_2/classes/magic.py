import random


class Spell:
    """docstring for ClassName"""
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type


    def generate_damage(self):
        """
        mg_l : magic low
        mg_h : magic high
        """
        mg_l = self.dmg - 15
        mg_h = self.dmg + 15
        return random.randrange(mg_l,mg_h)


