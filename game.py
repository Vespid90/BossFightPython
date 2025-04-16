from character import Player
from character import Monster
from stats import Stats
from text import Text
import random

player = Player("Hero")
monster = Monster("Monster")
# boss = Boss("Boss")
stats = Stats()
text = Text()


class Game:
    def __init__(self):
        self.name = "BossFight"

    def start_game(self):
        m = monster
        p = player
        text.text_speed("Les brumes du monde ancien s’épaississent... \nDans les ténèbres de la forêt d’Obsydor, des créatures oubliées s’éveillent...\nToi, humble aventurier, tu as entendu l’appel.\nTon voyage commence ici.")
        print("================================================")
        p.name = input("Quel est ton nom?: \n")
        print("================================================")
        text.text_speed(f"Je sens un grand pouvoir émané de toi, {p.name}....\nBienvenue dans l'univers de BossFight !")
        while p.level <= 100:
            start = input("Quelle action souhaites-tu faire ?: \n'a' pour avancer dans la forêt, \n's' pour voir les statistiques du personnage \n'q' pour quitter l'ancien monde: \n")
            if start == "a":
                print("================================================")
                alea = random.randint(0, 3)
                if alea == 0:
                    print("Un nouvel ennemi apparait !")
                    stats.stats(p, m)
                    if m.monster_level(p.level) > p.level:
                        p.health_lose(m.damage)
                        print(f"Outch ! Le {m.name} inflige {m.damage} dégâts")
                        print(f"Tu as maintenant {p.health} points de vie")
                        print("================================================")
                        if p.health <= 0:
                            print("Tu es mort au combat")
                            stats.stats_player(p)
                            quit()
                        else:
                            continue
                    else:
                        print(f"Bien joué {p.name}, tu as tué le {m.name} ! \nTu as gagné un niveau !!")
                        p.level_up()
                        p.health_up()
                        print(f"Tu es maintenant niveau {p.level} et tu as {p.health} points de vie")
                        print("================================================")
                        continue
                elif alea == 1:
                    print("Vous êtes tombé sur un piège ! vous perdez 3 points de vie")
                    p.health(3)
                elif alea == 2:
                    pass
                elif alea == 3:
                    print("Vous avez trouvé un objet !")
                else:
                    print("Vous avancez dans la forêt sombre")
                    continue
            elif start == "s":
                stats.stats_player(p)
            elif start == "q":
                print("Merci d'avoir joué ! A bientôt!")
                print("================================================")
                quit()
            else:
                print("Vous devez choisir entre 'a', 's' ou 'q' !")
                print("================================================")