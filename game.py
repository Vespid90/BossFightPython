from character import Player
from character import Monster
from stats import Stats
from text import Text
from fight import Fight
import random

player = Player("Hero")
monster = Monster("Monster")
# boss = Boss("Boss")
stats = Stats()
text = Text()
fight = Fight()


class Game:
    def __init__(self):
        self.name = "BossFight"

    def start_game(self):
        m = monster
        p = player
        text.title_speed(text.logo())
        text.text_speed(text.intro())
        text.separate_logic()
        p.name = input("Quel est votre nom?: \n")
        # text.clear_screen()
        text.separate_elem()
        text.text_speed(text.power(p.name))
        while p.level <= 100:
            menu = text.game_menu()
            if menu == "a":
                text.separate_logic()
                alea = random.randint(0, 0) #Début des événements aléatoires ; à adapter pour faire les tests
                text.text_speed("Vous avancez dans la forêt...")
                # ================= DEBUT COMBAT VS MONSTER =================
                if alea == 0:
                    text.new_enemy_appear()
                    lvl_enemy = m.monster_level(p.level)
                    if lvl_enemy > p.level:
                        stats.stats(p, m)
                        p.health_lose(m.damage)
                        text.take_damage(m.name, m.damage, p.health)
                        text.separate_logic()
                        if p.health <= 0:
                            text.p_dead()
                            stats.stats_player(p)
                            quit()
                        else:
                            continue
                    elif lvl_enemy <= p.level:
                        stats.stats(p, m)
                        text.e_killed(p.name, m.name)
                        p.level_up()
                        p.health_up()
                        text.lvl_up(p.level, p.health)
                        text.separate_logic()
                        continue
                    else:
                        stats.stats(p, m)
                        print("error")
                    # ================= FIN COMBAT VS MONSTER =================
                    # ================= DEBUT SYSTEME DE PIEGE =================
                elif alea == 1: #piege
                    p.health_lose(3)
                    text.trap_damages(p.health)
                    text.separate_logic()
                    if p.health <= 0:
                        text.p_dead()
                        stats.stats_player(p)
                        quit()
                    else:
                        continue
                elif alea == 2: #se blesse
                    p.health_lose(1)
                    print(f"Vous vous blessez en marchant ! Vous perdez 1 point de vie.")
                    print(f"Vous avez maintenant {p.health} ❤️ points de vie.")
                    text.separate_logic()
                    if p.health <= 0:
                        text.p_dead()
                        stats.stats_player(p)
                        quit()
                    else:
                        continue
                # ================= FIN SYSTEME DE PIEGE =================
                # ================= DEBUT SYSTEME D'OBJET =================
                elif alea == 3: #trouve un objet
                    obj = ["Explose", "Potion de soin", "Collier de soin", "Epée", "Bouclier", "Casque", "Armure", "Jambière", "Botte", "Gants", "Brassard", "Bombe"]
                    print("Vous fouillez les alentours...")
                    text.separate_elem()
                    objet = random.choice(obj)
                    if objet == "Potion de soin" or objet == "Collier de soin":
                        p.health_up()
                        if objet == "Potion de soin":
                            print(f"Vous avez trouvé une {objet}.")
                            print(f"Vous avez maintenant ❤️ {p.health} point(s) de vie.")
                            text.separate_logic()
                        else:
                            print(f"Vous avez trouvé un {objet}.")
                            print(f"Vous avez maintenant ❤️ {p.health} point(s) de vie.")
                            text.separate_logic()
                    elif objet == "Bombe":
                        p.inventory.append("Bombe")
                        print("Vous avez trouvé une 💣Bombe de fumée 💣. Elle vous servira à fuir un combat.")
                        text.separate_logic()
                    elif objet == "Explose":
                        if "bombe" in p.inventory:
                            p.health_lose(2)
                            p.inventory.remove("bombe")
                            print("Outch ! La bombe de fumée que vous aviez dans votre inventaire à 💥💥explosée 💥💥 ! Elle vous inflige 2 points de dégâts")
                            text.separate_logic()
                            if p.health <= 0:
                                text.p_dead()
                                stats.stats_player(p)
                                quit()
                            else:
                                continue
                        else:
                            print("Vous pensiez avoir trouvé quelque chose... ce n'était qu'un tas de purin.")
                            continue
                    else:
                        p.inventory.append(objet)
                        print(f"Vous avez trouvé l'objet {objet}.")
                        print("Vous l'ajoutez à votre inventaire")
                        text.separate_logic()
                # ================= FIN SYSTEME D'OBJET =================
                # ================= DEBUT VOYAGE FORET =================
                else: #avance dans la foret sans événements
                    text.text_speed("Tout semble calme, pour l'instant.")
                    continue
                # ================= FIN VOYAGE FORET =================
            elif menu == "s":
                stats.stats_player(p)
            elif menu == "q":
                print("Merci d'avoir joué ! A bientôt!")
                text.separate_logic()
                quit()
            else:
                print("Vous devez choisir entre 'a', 's' ou 'q' !")
                text.separate_logic()