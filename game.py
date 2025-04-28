from character import Player
from character import Monster
from stuff import available_stuff
from stats import Stats
from text import TextDialogue, TextFight, TextItem, Interface, TextForest
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
        # i = player.stuff.values
        # TextDialogue.title_speed(Interface.logo())
        # TextDialogue.text_speed(TextDialogue.intro())
        # Interface.separate_logic()
        p.name = TextDialogue.player_name()
        # Text.clear_screen()
        Interface.separate_elem()
        TextDialogue.text_speed(TextDialogue.power(p.name))
        while p.level <= 100:
            menu = TextDialogue.game_menu()
            # ================= DEBUT MENU DU DIALOGUE ==================
            if menu == "a":
                Interface.separate_logic()
                # Début des événements aléatoires ; variable "alea" à adapter pour les tests
                # 0 = combats ; 1 = piege ; 2 = se blesse ; 3 = trouve un objet ;
                alea = random.randint(3, 3)
                TextDialogue.text_speed(TextDialogue.go_wood())
                # ================= DEBUT COMBAT VS MONSTER =================
                if alea == 0:
                    try:
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
                    except TypeError:
                        print("Error in combat system")
                # ================= FIN COMBAT VS MONSTER ==================
                # ================= DEBUT SYSTEME DE PIEGE =================
                elif alea == 1: #piege
                    try:
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
                    except TypeError:
                        print("Error in trap system")
                # ================= FIN SYSTEME DE PIEGE =================
                # ================= DEBUT SYSTEME SE BLESSE =================
                elif alea == 2: #se blesse
                    try:
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
                    except TypeError:
                        print("Error in injure system")
                # ================= FIN SYSTEME SE BLESSE =================
                # ================= DEBUT SYSTEME D'OBJET ================
                elif alea == 3: #trouve un objet
                    try:
                        obj = available_stuff
                        TextItem.go_search()
                        Interface.separate_elem()
                        objet = random.choice(obj)
                        if objet.name == "Potion de soin" or objet.name == "Collier de soin":
                            p.health_up()
                            if objet == "Potion de soin":
                                TextItem.healing_pot(objet, p.health)
                                Interface.separate_logic()
                            else:
                                TextItem.healing_neck(objet, p.health)
                                Interface.separate_logic()
                        elif objet.name == "Bombe":
                            p.inventory.append("Bombe")
                            TextItem.find_bomber()
                            Interface.separate_logic()
                        elif objet.name == "Explose":
                            if objet.name == "Bombe" in p.inventory:
                                health_lose = 2
                                p.health_lose(health_lose)
                                p.inventory.remove("Bombe")
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
                            p.equip(objet.name)
                            Interface.separate_logic()
                    except TypeError:
                        print("Error in loot item system")
                # ================= FIN SYSTEME D'OBJET =================
                # ================= DEBUT VOYAGE FORET ==================
                else: #avance dans la foret sans événements
                    TextDialogue.text_speed(TextForest.calm())
                    continue
                # ================= FIN VOYAGE FORET =================
            # ================= AUTRE CHOIX DU DIALOGUE ==================
            elif menu == "s":
                Stats.stats_player(p)
            elif menu == "q":
                TextDialogue.thanks_for_playing()
                Interface.separate_logic()
                quit()
            else:
                TextDialogue.need_to_choice()
                Interface.separate_logic()