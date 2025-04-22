

class Stuff:
    def __init__(self, name, stat_type, value, slot):
        self.name = name
        self.stat_type = stat_type
        self.value = value
        self.slot = slot


available_stuff = [
    Stuff("Epée", "damage", 1, "main_hand"),
    Stuff("Bouclier", "defense", 2, "off_hand"),
    Stuff("Casque", "defense", 1, "head"),
    Stuff("Armure", "defense", 3, "torso"),
    Stuff("Jambière", "defense", 3, "legs"),
    Stuff("Botte", "defense", 1, "feet"),
    Stuff("Gants", "defense", 1, "hands"),
    Stuff("Brassard", "defense", 1, "arms"),
]
