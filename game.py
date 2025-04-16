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
                elif alea == 1: #piege -3 hp
                    p.health_lose(3)
                    print("Vous êtes tombé sur un piège ! vous perdez 3 points de vie")
                    print(f"Tu as maintenant {p.health} points de vie")
                    print("================================================")
                    if p.health <= 0:
                        print("Tu es mort au combat")
                        stats.stats_player(p)
                        quit()
                    else:
                        continue
                elif alea == 2: #se blesse - 1hp
                    p.health_lose(1)
                    print("Vous vous blessez en marchant ! vous perdez 1 point1 de vie")
                    print(f"Tu as maintenant {p.health} points de vie")
                    print("================================================")
                    if p.health <= 0:
                        print("Tu es mort au combat")
                        stats.stats_player(p)
                        quit()
                    else:
                        continue
                elif alea == 3: #trouve un objet ; potion(+2 à +5 hp), bombe de fumée(fuite combat) (?)
                    print("Vous avez trouvé un objet !")
                    objet = random.randint(0, 1)
                    if objet == 0:
                        p.health_up()
                        print("Vous avez trouvé une potion de soin !")
                        print(f"Vous avez maintenant {p.health} point de vie")
                    else:
                        print("Vous avez trouvé une bombe de fumée ! Elle vous servira à fuir un combat ")
                        # p_inventory.append(bombe) -> créer un inventaire
                else: #avance dans la foret sans événements
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