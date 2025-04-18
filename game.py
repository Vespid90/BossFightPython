from character import Player
from character import Monster
from stats import Stats
from text import TextDialogue, TextFight, TextItem, Interface
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
        # TextDialogue.title_speed(Interface.logo())
        # TextDialogue.text_speed(TextDialogue.intro())
        # Interface.separate_logic()
        p.name = TextDialogue.player_name()
        # Text.clear_screen()
        Interface.separate_elem()
        TextDialogue.text_speed(TextDialogue.power(p.name))
        while p.level <= 100:
            menu = TextDialogue.game_menu()
            if menu == "a":
                Interface.separate_logic()
                # Début des événements aléatoires ; variable "alea" à adapter pour les tests
                # 0 = combats ; 1 = piege ; 2 = se blesse ; 3 = trouve un objet ;
                alea = random.randint(3, 3)
                TextDialogue.text_speed(TextDialogue.go_wood())
                # ================= DEBUT COMBAT VS MONSTER =================
                if alea == 0:
                    TextFight.new_enemy_appear()
                    lvl_enemy = m.monster_level(p.level)
                    if lvl_enemy > p.level:
                        Stats.stats(p, m)
                        p.health_lose(m.damage)
                        TextFight.take_damage(m.name, m.damage, p.health)
                        Interface.separate_logic()
                        if p.health <= 0:
                            TextFight.p_dead()
                            Stats.stats_player(p)
                            quit()
                        else:
                            continue
                    elif lvl_enemy <= p.level:
                        Stats.stats(p, m)
                        TextFight.e_killed(p.name, m.name)
                        p.level_up()
                        TextFight.lvl_up(p.level, p.health)
                        Interface.separate_logic()
                        continue
                    else:
                        Stats.stats(p, m)
                        print("error")
                    # ================= FIN COMBAT VS MONSTER =================
                    # ================= DEBUT SYSTEME DE PIEGE =================
                elif alea == 1: #piege
                    health_lose = 3
                    p.health_lose(health_lose)
                    TextFight.trap_damages(health_lose, p.health)
                    Interface.separate_logic()
                    if p.health <= 0:
                        TextFight.p_dead()
                        Stats.stats_player(p)
                        quit()
                    else:
                        continue
                elif alea == 2: #se blesse
                    health_lose = 1
                    p.health_lose(health_lose)
                    TextFight.walk_damage(health_lose,p.health)
                    Interface.separate_logic()
                    if p.health <= 0:
                        TextFight.p_dead()
                        Stats.stats_player(p)
                        quit()
                    else:
                        continue
                # ================= FIN SYSTEME DE PIEGE =================
                # ================= DEBUT SYSTEME D'OBJET =================
                elif alea == 3: #trouve un objet
                    obj = TextItem.obj()
                    TextItem.go_search()
                    Interface.separate_elem()
                    objet = random.choice(obj)
                    if objet == "Potion de soin" or objet == "Collier de soin":
                        p.health_up()
                        if objet == "Potion de soin":
                            TextItem.healing_pot(objet, p.health)
                            Interface.separate_logic()
                        else:
                            TextItem.healing_neck(objet, p.health)
                            Interface.separate_logic()
                    elif objet == "Bombe":
                        p.inventory.append("Bombe")
                        TextItem.find_bomber()
                        Interface.separate_logic()
                    elif objet == "Explose":
                        if "bombe" in p.inventory:
                            health_lose = 2
                            p.health_lose(health_lose)
                            p.inventory.remove("bombe")
                            TextItem.explose_bomber(health_lose)
                            Interface.separate_logic()
                            if p.health <= 0:
                                TextFight.p_dead()
                                Stats.stats_player(p)
                                quit()
                            else:
                                continue
                        else:
                            TextItem.shit()
                            continue
                    else:
                        p.inventory.append(objet)
                        TextItem.find_item(objet)
                        Interface.separate_logic()
                # ================= FIN SYSTEME D'OBJET =================
                # ================= DEBUT VOYAGE FORET =================
                else: #avance dans la foret sans événements
                    TextDialogue.text_speed("Tout semble calme, pour l'instant.")
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