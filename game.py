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
        print("═════════════════════════════════════════════════")
        p.name = input("Quel est votre nom?: \n")
        print("=================================================")
        text.text_speed(f"Je sens un grand pouvoir émané de vous, {p.name}....\nBienvenue dans l'univers de BossFight !")
        while p.level <= 100:
            start = input("Quelle action souhaitez-vous faire ?: \n'a' pour avancer dans la forêt, \n's' pour voir les statistiques du personnage \n'q' pour quitter la fôret d'Obsydor: \n")
            if start == "a":
                print("═════════════════════════════════════════════════")
                alea = random.randint(0, 3) #Début des événements aléatoires
                text.text_speed("Vous avancez dans la forêt...")
                # ================= DEBUT COMBAT VS MONSTER =================
                if alea == 0:
                    print("Un nouvel ennemi apparait !")
                    lvl_enemy = m.monster_level(p.level)
                    if lvl_enemy > p.level:
                        stats.stats(p, m)
                        p.health_lose(m.damage)
                        print(f"Outch ! Le {m.name} inflige ⚔️ {m.damage} dégâts.")
                        print(f"Vous avez maintenant ❤️ {p.health} points de vie.")
                        print("═════════════════════════════════════════════════")
                        if p.health <= 0:
                            print("Vous êtes mort au combat.")
                            stats.stats_player(p)
                            quit()
                        else:
                            continue
                    elif lvl_enemy <= p.level:
                        stats.stats(p, m)
                        print(f"Bien joué {p.name}, vous avez tué le {m.name} ! \nVous avez gagné un niveau 🆙!")
                        p.level_up()
                        p.health_up()
                        print(f"Vous êtes maintenant niveau ⬆️ {p.level} et vous avez {p.health} ❤️ points de vie.")
                        print("═════════════════════════════════════════════════")
                        continue
                    else:
                        stats.stats(p, m)
                        print("error")
                    # ================= FIN COMBAT VS MONSTER =================
                    # ================= DEBUT SYSTEME DE PIEGE =================
                elif alea == 1: #piege
                    p.health_lose(3)
                    print("Vous êtes tombé sur un piège ! vous perdez 3 points de vie.")
                    print(f"Vous avez maintenant {p.health} ❤️ points de vie.")
                    print("═════════════════════════════════════════════════")
                    if p.health <= 0:
                        print("Vous êtes mort au combat.")
                        stats.stats_player(p)
                        quit()
                    else:
                        continue
                elif alea == 2: #se blesse
                    p.health_lose(1)
                    print("Vous vous blessez en marchant ! Vous perdez 1 point de vie.")
                    print(f"Vous avez maintenant {p.health} ❤️ points de vie.")
                    print("═════════════════════════════════════════════════")
                    if p.health <= 0:
                        print("Vous êtes mort au combat.")
                        stats.stats_player(p)
                        quit()
                    else:
                        continue
                # ================= FIN SYSTEME DE PIEGE =================
                # ================= DEBUT SYSTEME D'OBJET =================
                elif alea == 3: #trouve un objet
                    obj = ["Explose", "Potion de soin", "Collier de soin", "Epée", "Bouclier", "Casque", "Armure", "Jambière", "Botte", "Gants", "Brassard", "Bombe"]
                    print("Vous fouillez les alentours...")
                    objet = random.choice(obj)
                    if objet == "Potion de soin" or objet == "Collier de soin":
                        p.health_up()
                        if objet == "Potion de soin":
                            print(f"Vous avez trouvé une {objet}.")
                            print(f"Vous avez maintenant ❤️ {p.health} point(s) de vie.")
                        else:
                            print(f"Vous avez trouvé un {objet}.")
                            print(f"Vous avez maintenant ❤️ {p.health} point(s) de vie.")
                    elif objet == "Bombe":
                        p.inventory.append("Bombe")
                        print("Vous avez trouvé une 💣Bombe de fumée 💣. Elle vous servira à fuir un combat.")
                    elif objet == "Explose":
                        if "bombe" in p.inventory:
                            p.health_lose(2)
                            p.inventory.remove("bombe")
                            print("Outch ! La bombe de fumée que vous aviez dans votre inventaire à 💥💥explosée 💥💥 ! Elle vous inflige 2 points de dégâts")
                        else:
                            print("Vous pensiez avoir trouvé quelque chose... ce n'était qu'un tas de purin.")
                            continue
                    else:
                        p.inventory.append(objet)
                        print(f"Vous avez trouvé l'objet {objet}.")
                        print("Vous l'ajoutez à votre inventaire")
                # ================= FIN SYSTEME D'OBJET =================
                # ================= DEBUT VOYAGE FORET =================
                else: #avance dans la foret sans événements
                    text.text_speed("Tout semble calme, pour l'instant.")
                    continue
                # ================= FIN VOYAGE FORET =================
            elif start == "s":
                stats.stats_player(p)
            elif start == "q":
                print("Merci d'avoir joué ! A bientôt!")
                print("═════════════════════════════════════════════════")
                quit()
            else:
                print("Vous devez choisir entre 'a', 's' ou 'q' !")
                print("═════════════════════════════════════════════════")
