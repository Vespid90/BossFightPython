import random


class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.health = hp
        self.level = 0

    def attack(self, player):
        return player.health_lose

    def enemy_level(self, player_level):
        return random.randint(-1,1)

    def __str__(self):
        return f'name:{self.name}, health:{self.health}, level:{self.enemy_level()}'