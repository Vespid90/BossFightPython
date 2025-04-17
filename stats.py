from text import Text

text = Text()

class Stats:
    def __init__(self):
        self.name = "Stats"
    def stats(self, pl, en):
        print(f"{'Le combat commence:':<26}")
        text.separate_logic()
        print(f"Nom: {pl.name:<20} Nom: {en.name:<20}")
        print(f"⬆️ Niveau: {pl.level:<14} ⬆️ Niveau: {en.level:<20}")
        print(f"❤️ Vie: {pl.health:<16}️ ❤️ Vie: {en.health:<20}")
        print(f"⚔️ Dégâts: {pl.damage:<14} ⚔️ Dégâts: {en.attack():<20}")
        # print(f"🛡️ Défense: {pl.defense: <20} 🛡️ Défense: {en.defense: <20}️")
        text.separate_logic()

    def stats_player(self, pl):
        text.separate_logic()
        print("Stats du Héro")
        text.separate_elem()
        print(f"Nom: {pl.name}")
        print(f"⬆️ Niveau: {pl.level}")
        print(f"❤️ Vie: {pl.health}️")
        print(f"⚔️ Dégâts: {pl.damage:<20}")
        # print(f"🛡️ Défense: {pl.defense: <20}")
        text.separate_elem()
        print("🎒 Inventaire: ")
        print(f"{pl.inventory}")
        text.separate_logic()
