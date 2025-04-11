import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 5
        self.level = 1

    def health_lose(self,enemy_attack):
        self.health -= enemy_attack
        return self.health

    def health_up(self):
        self.health = random.randint(self.health + 2, self.health + 5)
        return self.health

    def level_up(self):
        self.level += 1

    def __str__(self):
        return f'name:{self.name}, health:{self.health}, level:{self.level}'
