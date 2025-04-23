from text import Interface

class Stats:
    def __init__(self):
        self.name = "Stats"

    @staticmethod
    def stats(pl, en):
        print(f"{'Le combat commence:':<26}")
        Interface.separate_logic()
        print(f"Nom: {pl.name:<20} Nom: {en.name:<20}")
        print(f"⬆️ Niveau: {pl.level:<14} ⬆️ Niveau: {en.level:<20}")
        print(f"❤️ Vie: {pl.health:<16}️ ❤️ Vie: {en.health_up():<20}")
        print(f"⚔️ Dégâts: {pl.damage:<14} ⚔️ Dégâts: {en.attack():<20}")
        print(f"🛡️ Défense: {pl.defense: <13} 🛡️ Défense: {en.defense_up(): <20}️")
        Interface.separate_logic()

    @staticmethod
    def stats_player(pl):
        Interface.separate_logic()
        print("Stats du Héro")
        Interface.separate_elem()
        print(f"Nom: {pl.name}")
        print(f"⬆️ Niveau: {pl.level}")
        print(f"❤️ Vie: {pl.health}")
        print(f"⚔️ Dégâts: {pl.damage:<20}")
        print(f"🛡️️ Défense: {pl.defense: <20}")
        Interface.separate_elem()
        print("🎒 Inventaire: ")
        print(f"{pl.inventory}")
        Interface.separate_elem()
        print("Stuff équipé: ")
        for key, value in pl.stuff.items():
            if value is not None:
                print(f"{key:<18}: {value.name}")
            else:
                print(f"{key:<18}: ")
        Interface.separate_logic()
