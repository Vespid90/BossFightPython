class Player:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.health = hp
        self.level = lvl

    def health_lose(self):
        self.health -= 1

    def health_up(self):
        self.health += 2

    def level_up(self):
        self.level += 1

    def __str__(self):
        return f'name:{self.name}, health:{self.health}, level:{self.level}'
