import random

class Enemy:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.health = hp
        self.level = lvl

    # def attack(self, player):
    #     return player.health_lose()

    def enemy_level(self, player_level):
        return random.randint(player_level-1,player_level+1)

    def __str__(self):
        return f'name:{self.name}, health:{self.health}, level:{self.enemy_level()}'