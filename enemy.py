import random

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.level = 1
        self.damage = 0

    def enemy_level(self, player_level):
        self.level = random.randint(player_level-1,player_level+1)
        return self.level

    def attack(self):
        self.damage = random.randint(self.level +1, self.level +2)
        return self.damage

    def __str__(self):
        return f'Nom:{self.name}, vie:{self.health}, niveau:{self.level}'