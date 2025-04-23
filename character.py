import random

class Character:
    def __init__(self, name, hp, lvl, dmg, deff):
        self.name = name
        self.health = hp
        self.level = lvl
        self.damage = dmg
        self.defense = deff

    def health_lose(self,character_attack):
        damage_taken = (character_attack - (character_attack/100*self.defense))
        self.health -= max(0, damage_taken)
        return self.health

    def health_up(self):
        self.health += random.randint( 1, 2)
        return self.health

    def attack(self):
        self.damage = random.randint(self.level + 1, self.level + 3)
        return self.damage

    def defense_up(self):
        self.defense = random.randint(int(self.defense) + 0, int(self.defense) + 2)
        return self.defense

    def __str__(self):
        return f'Nom:{self.name}, ❤️ vie:{self.health}, ⬆️ niveau:{self.level}'



class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=5, lvl=1, dmg=2, deff=1)
        self.inventory = []
        self.stuff = {"Tête": None, "Torse": None, "Jambes": None, "Pieds": None, "Bras": None, "Main secondaire": None, "Main principale": None, "Mains": None, "Collier": None, "Bague": None, "Potion": None}

    def level_up(self):
        self.level += 1
        self.health += random.randint(1, 2)
        self.damage += random.randint(2, 4)
        self.defense += random.randint(1, 2)


    def equip(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.stuff[item.slot] = item
                #voir la logique à appliquer pour gérer les bombes et potions de soins
                # if self.stuff[item.slot] == item:
                self.inventory.remove(item)
                print(f"{self.name} a équipé {item.name} (slot: {item.slot})")



class Monster(Character):
    def __init__(self, name):
        super().__init__(name,hp=3,lvl=2,dmg=0,deff=0)

    def monster_level(self, player_level):
        self.level = random.randint(max(1,player_level-1),player_level+1)
        return self.level

    def health_up(self):
        self.health = random.randint(self.health + 1, self.health + 2)
        return self.health

    def attack(self):
        self.damage = random.randint(self.level +1, self.level +3)
        return self.damage

    def defense_up(self):
        self.defense = random.randint(int(self.defense) + 0, int(self.defense) + 2)
        return self.defense



# class Boss:
#     def __init__(self, name):
#         self.name = name
#         self.health = 20
#         self.level = 10
#         self.damage = 30
#         self.defense = 15
#
#     def boss_level(self, player_level):
#         self.level = random.randint(player_level - 1, player_level + 1)
#         return self.level
#
#     def attack(self):
#         self.damage = random.randint(self.level +1, self.level +2)
#         return self.damage
#
#     def defense_up(self):
#         self.defense = random.randint(self.defense + 0, self.defense + 2)
#         return self.defense
#
#     def __str__(self):
#         return f'Nom:{self.name}, ❤️ vie:{self.health}, ⬆️ niveau:{self.level}'