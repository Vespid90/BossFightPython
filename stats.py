class Stats:
    def __init__(self):
        self.name = "Stats"
    def stats(self, pl, en):
        print(f"{'Le combat commence:':<26}")
        print("═════════════════════════════════════════════════")
        print(f"Nom: {pl.name:<20} Nom: {en.name:<20}")
        print(f"⬆️ Niveau: {pl.level:<17} ⬆️ Niveau: {en.level:<20}")
        print(f"❤️ Vie: {pl.health:<20}️ ❤️Vie: {en.health:<20}")
        print(f"⚔️ Dégâts: {pl.damage:<20} ⚔️ Dégâts: {en.attack():<20}")
        print(f"🛡️ Défense: {pl.defense: <20} 🛡️ Défense: {en.defense: <20}️")
        print("═════════════════════════════════════════════════")

    def stats_player(self, pl):
        print("═════════════════════════════════════════════════")
        print("Stats du Héro")
        print("=================================================")
        print(f"Nom: {pl.name}")
        print(f"⬆️ Niveau: {pl.level}")
        print(f"❤️ Vie: {pl.health}️")
        print(f"⚔️ Dégâts: {pl.damage:<20}")
        print(f"🛡️ Défense: {pl.defense: <20}")
        print("=================================================")
        print("🎒 Inventaire: ")
        print(f"{pl.inventory}")
        print("═════════════════════════════════════════════════")
