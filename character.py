import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 5
        self.level = 1
        self.damage = 2
        self.defense = 1
        self.inventory = []

    def health_lose(self,enemy_attack):
        self.health -= (enemy_attack - (enemy_attack/100*self.defense))
        return self.health

    def level_up(self):
        self.level += 1
        self.health = random.randint(int(self.health) + 1, int(self.health) + 2)
        self.damage = random.randint(int(self.level) + 2, int(self.level) + 4)
        self.defense = random.randint(int(self.defense) + 1, int(self.defense) + 2)

    def health_up(self):
        self.health = random.randint(int(self.health) + 2, int(self.health) + 5)
        return self.health

    def __str__(self):
        return f'Nom:{self.name}, ❤️ vie:{self.health}, ⬆️ niveau:{self.level}'



class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.level = 1
        self.damage = 0
        self.defense = 0

    def monster_level(self, player_level):
        self.level = random.randint(player_level-1,player_level+1)
        return self.level

    def health_lose(self,player_attack):
        self.health -= (player_attack - (player_attack/100*self.defense))
        return self.health

    def health_up(self):
        self.health = random.randint(self.health + 1, self.health + 2)
        return self.health

    def attack(self):
        self.damage = random.randint(self.level +1, self.level +3)
        return self.damage

    def defense_up(self):
        self.defense = random.randint(self.defense + 0, self.defense + 2)
        return self.defense

    def __str__(self):
        return f'Nom:{self.name}, ❤️ vie:{self.health}, ⬆️ niveau:{self.level}'



class Boss:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.level = 10
        self.damage = 30
        self.defense = 15

    def boss_level(self, player_level):
        self.level = random.randint(player_level - 1, player_level + 1)
        return self.level

    def attack(self):
        self.damage = random.randint(self.level +1, self.level +2)
        return self.damage

    def defense_up(self):
        self.defense = random.randint(self.defense + 0, self.defense + 2)
        return self.defense

    def __str__(self):
        return f'Nom:{self.name}, ❤️ vie:{self.health}, ⬆️ niveau:{self.level}'