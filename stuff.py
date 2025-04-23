class Stuff:
    def __init__(self, name, stat_type, value, slot):
        self.name = name
        self.stat_type = stat_type
        self.value = value
        self.slot = slot


available_stuff = [
    Stuff("Epée", "damage", 1, "Main principale"),
    Stuff("Bouclier", "defense", 2, "Main secondaire"),
    Stuff("Casque", "defense", 1, "Tête"),
    Stuff("Armure", "defense", 3, "Torse"),
    Stuff("Jambière", "defense", 3, "Jambes"),
    Stuff("Botte", "defense", 1, "Pieds"),
    Stuff("Gants", "defense", 1, "Mains"),
    Stuff("Brassard", "defense", 1, "Bras"),
    Stuff("Collier de soin", "health", 5, "Collier"),
    Stuff("Bague", "health", 2, "Bague")
]
