class Stuff:
    def __init__(self, name, stat_type, value, slot):
        self.name = name
        self.stat_type = stat_type
        self.value = value
        self.slot = slot


available_stuff = [
    Stuff("Epée tranchante", "damage", 1, "Main principale"),
    Stuff("Bouclier rond", "defense", 2, "Main secondaire"),
    Stuff("Casque lourd", "defense", 1, "Tête"),
    Stuff("Armure lourde", "defense", 3, "Torse"),
    Stuff("Jambière lourde", "defense", 3, "Jambes"),
    Stuff("Botte lourde", "defense", 1, "Pieds"),
    Stuff("Gants en mailles", "defense", 1, "Mains"),
    Stuff("Brassard en mailles", "defense", 1, "Bras"),
    Stuff("Collier de soin", "health", 5, "Collier"),
    Stuff("Bague protectrice", "health", 2, "Bague")
]
