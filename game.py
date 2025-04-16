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
        text.text_speed("Les brumes du monde ancien s’épaississent... \nDans les ténèbres de la forêt d’Obsydor, des créatures oubliées s’éveillent...\nVous, humble aventurier, vous avez entendu l’appel.\nVotre voyage commence ici.")
        print("================================================")
        p.name = input("Quel est votre nom?: \n")
        print("================================================")
        text.text_speed(f"Je sens un grand pouvoir émané de vous, {p.name}....\nBienvenue dans l'univers de BossFight !")
        while p.level <= 100:
            start = input("Quelle action souhaitez-vous faire ?: \n'a' pour avancer dans la forêt, \n's' pour voir les statistiques du personnage \n'q' pour quitter la fôret d'Obsydor: \n")
            if start == "a":
                print("================================================")
                alea = random.randint(0, 3) #Début des événements aléatoires
                text.text_speed("Vous avancez das la forêt...")
                if alea == 0: #monster
                    print("Un nouvel ennemi apparait !")
                    stats.stats(p, m)
                    if m.monster_level(p.level) > p.level:
                        p.health_lose(m.damage)
                        print(f"Outch ! Le {m.name} inflige {m.damage} dégâts.")
                        print(f"Vous avez maintenant {p.health} points de vie.")
                        print("================================================")
                        if p.health <= 0:
                            print("Vous êtes mort au combat.")
                            stats.stats_player(p)
                            quit()
                        else:
                            continue
                    else:
                        print(f"Bien joué {p.name}, vous avez tué le {m.name} ! \nVous avez gagné un niveau !!")
                        p.level_up()
                        p.health_up()
                        print(f"Vous êtes maintenant niveau {p.level} et vous avez {p.health} points de vie.")
                        print("================================================")
                        continue
                elif alea == 1: #piege
                    p.health_lose(3)
                    print("Vous êtes tombé sur un piège ! vous perdez 3 points de vie.")
                    print(f"Vous avez maintenant {p.health} points de vie.")
                    print("================================================")
                    if p.health <= 0:
                        print("Vous êtes mort au combat.")
                        stats.stats_player(p)
                        quit()
                    else:
                        continue
                elif alea == 2: #se blesse
                    p.health_lose(1)
                    print("Vous vous blessez en marchant ! Vous perdez 1 point de vie.")
                    print(f"Vous avez maintenant {p.health} points de vie.")
                    print("================================================")
                    if p.health <= 0:
                        print("Vous êtes mort au combat.")
                        stats.stats_player(p)
                        quit()
                    else:
                        continue
                elif alea == 3: #trouve un objet
                    print("Vous fouillez les alentours...")
                    objet = random.randint(0, 10)
                    if objet == 0:
                        p.health_up()
                        print("Vous avez trouvé une potion de soin.")
                        print(f"Vous avez maintenant {p.health} point de vie.")
                    elif objet == 1:
                        p.inventory.append("Epée")
                        print("Vous avez trouvé une Epée.")
                    elif objet == 2:
                        p.inventory.append("Bouclier")
                        print("Vous avez trouvé un Bouclier.")
                    elif objet == 3:
                        p.inventory.append("Casque")
                        print("Vous avez trouvé un Casque.")
                    elif objet == 4:
                        p.inventory.append("Armure")
                        print("Vous avez trouvé une Armure.")
                    elif objet == 5:
                        p.inventory.append("Jambière")
                        print("Vous avez trouvé une Jambière.")
                    elif objet == 6:
                        p.inventory.append("Botte")
                        print("Vous avez trouvé une paire de Botte.")
                    elif objet == 7:
                        p.inventory.append("Gants")
                        print("Vous avez trouvé une paire de Gants.")
                    elif objet == 8:
                        p.inventory.append("Brassard")
                        print("Vous avez trouvé un Brassard.")
                    elif objet == 9:
                        p.inventory.append("bombe")
                        print("Vous avez trouvé une bombe de fumée. Elle vous servira à fuir un combat.")
                    elif objet == 10:
                        bombe = p.inventory("bombe")
                        if bombe in p.inventory:
                            p.health_lose(2)
                            p.inventory.remove("bombe")
                            print("Outch ! La bombe de fumée que vous aviez dans votre inventaire à explosée ! Elle vous inflige 2 points de dégâts")
                        else:
                            continue
                    else:
                        print("Vous pensiez avoir trouvé quelque chose... ce n'était qu'un tas de purin.")
                else: #avance dans la foret sans événements
                    text.text_speed("Tout semble calme, pour l'instant.")
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