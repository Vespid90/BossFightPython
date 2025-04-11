import random



class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.level = 0
        self.damage = 0

    def attack(self):
        # return player.health_lose()
        self.damage = random.randint(1, 3)
        return self.damage

    def enemy_level(self, player_level):
        self.level = random.randint(player_level-1,player_level+1)
        return self.level

    def __str__(self):
        return f'name:{self.name}, health:{self.health}, level:{self.level}'