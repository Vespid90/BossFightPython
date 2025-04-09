class Player:
    def __init__(self):
        self.health = 5
        self.level = 1

    def level_up(self):
        self.level += 1

    def health_down(self):
        self.health -= 1