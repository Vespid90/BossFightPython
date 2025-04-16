import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 5
        self.level = 1
        self.inventory = []
        self.damage = 3

    def health_lose(self,enemy_attack):
        self.health -= enemy_attack
        return self.health

    def health_up(self):
        self.health = random.randint(self.health + 4, self.health + 7)
        return self.health

    def attack(self):
        self.damage += random.randint(self.level + 1, self.level + 2)
        return self.damage

    def level_up(self):
        self.level += 1

    def __str__(self):
        return f'Nom:{self.name}, vie:{self.health}, niveau:{self.level}'

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.level = 1
        self.damage = 0

    def monster_level(self, player_level):
        self.level = random.randint(player_level-1,player_level+1)
        return self.level

    def attack(self):
        self.damage = random.randint(self.level +1, self.level +2)
        return self.damage

    def __str__(self):
        return f'Nom:{self.name}, vie:{self.health}, niveau:{self.level}'

class Boss:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.level = 10
        self.damage = 30

    def boss_level(self, player_level):
        self.level = random.randint(player_level - 1, player_level + 1)
        return self.level

    def attack(self):
        self.damage = random.randint(self.level +1, self.level +2)
        return self.damage

    def __str__(self):
        return f'Nom:{self.name}, vie:{self.health}, niveau:{self.level}'