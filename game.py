from character import Player
from character import Monster
from stats import Stats
from text import Text, Interface
import random

player = Player("Hero")
monster = Monster("Monster")
# boss = Boss("Boss")

class Game:
    def __init__(self):
        self.name = "BossFight"

    @staticmethod
    def start_game():
        m = monster
        p = player
        Text.title_speed(Interface.logo())
        Text.text_speed(Text.intro())
        Interface.separate_logic()
        p.name = Text.player_name()
        # Text.clear_screen()
        Interface.separate_elem()
        Text.text_speed(Text.power(p.name))
        while p.level <= 100:
            menu = Text.game_menu()
            if menu == "a":
                Interface.separate_logic()
                alea = random.randint(0, 0) #Début des événements aléatoires ; à adapter pour faire les tests
                Text.text_speed(Text.go_wood())
                # ================= DEBUT COMBAT VS MONSTER =================
                if alea == 0:
                    Text.new_enemy_appear()
                    lvl_enemy = m.monster_level(p.level)
                    if lvl_enemy > p.level:
                        Stats.stats(p, m)
                        p.health_lose(m.damage)
                        Text.take_damage(m.name, m.damage, p.health)
                        Interface.separate_logic()
                        if p.health <= 0:
                            Text.p_dead()
                            Stats.stats_player(p)
                            quit()
                        else:
                            continue
                    elif lvl_enemy <= p.level:
                        Stats.stats(p, m)
                        Text.e_killed(p.name, m.name)
                        p.level_up()
                        p.health_up()
                        Text.lvl_up(p.level, p.health)
                        Interface.separate_logic()
                        continue
                    else:
                        Stats.stats(p, m)
                        print("error")
                    # ================= FIN COMBAT VS MONSTER =================
                    # ================= DEBUT SYSTEME DE PIEGE =================
                elif alea == 1: #piege
                    p.health_lose(3)
                    Text.trap_damages(p.health)
                    Interface.separate_logic()
                    if p.health <= 0:
                        Text.p_dead()
                        Stats.stats_player(p)
                        quit()
                    else:
                        continue
                elif alea == 2: #se blesse
                    p.health_lose(1)
                    print(f"Vous vous blessez en marchant ! Vous perdez 1 point de vie.")
                    print(f"Vous avez maintenant {p.health} ❤️ points de vie.")
                    Interface.separate_logic()
                    if p.health <= 0:
                        Text.p_dead()
                        Stats.stats_player(p)
                        quit()
                    else:
                        continue
                # ================= FIN SYSTEME DE PIEGE =================
                # ================= DEBUT SYSTEME D'OBJET =================
                elif alea == 3: #trouve un objet
                    obj = ["Explose", "Potion de soin", "Collier de soin", "Epée", "Bouclier", "Casque", "Armure", "Jambière", "Botte", "Gants", "Brassard", "Bombe"]
                    print("Vous fouillez les alentours...")
                    Interface.separate_elem()
                    objet = random.choice(obj)
                    if objet == "Potion de soin" or objet == "Collier de soin":
                        p.health_up()
                        if objet == "Potion de soin":
                            print(f"Vous avez trouvé une {objet}.")
                            print(f"Vous avez maintenant ❤️ {p.health} point(s) de vie.")
                            Interface.separate_logic()
                        else:
                            print(f"Vous avez trouvé un {objet}.")
                            print(f"Vous avez maintenant ❤️ {p.health} point(s) de vie.")
                            Interface.separate_logic()
                    elif objet == "Bombe":
                        p.inventory.append("Bombe")
                        print("Vous avez trouvé une 💣Bombe de fumée 💣. Elle vous servira à fuir un combat.")
                        Interface.separate_logic()
                    elif objet == "Explose":
                        if "bombe" in p.inventory:
                            p.health_lose(2)
                            p.inventory.remove("bombe")
                            print("Outch ! La bombe de fumée que vous aviez dans votre inventaire à 💥💥explosée 💥💥 ! Elle vous inflige 2 points de dégâts")
                            Interface.separate_logic()
                            if p.health <= 0:
                                Text.p_dead()
                                Stats.stats_player(p)
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
                        Interface.separate_logic()
                # ================= FIN SYSTEME D'OBJET =================
                # ================= DEBUT VOYAGE FORET =================
                else: #avance dans la foret sans événements
                    Text.text_speed("Tout semble calme, pour l'instant.")
                    continue
                # ================= FIN VOYAGE FORET =================
            elif menu == "s":
                Stats.stats_player(p)
            elif menu == "q":
                print("Merci d'avoir joué ! A bientôt!")
                Interface.separate_logic()
                quit()
            else:
                print("Vous devez choisir entre 'a', 's' ou 'q' !")
                Interface.separate_logic()