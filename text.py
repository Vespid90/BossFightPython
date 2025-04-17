# from game import monster
# from game import player
import random
import time
import sys
import os


# m = monster
# p = player

class Text():
    def __init__(self):
        self.name = "text"

    def text_speed(self, texte, delai=0.01):
        for i in texte:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(delai)
        print()

    def title_speed(self, texte, delai=0.002):
        for i in texte:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(delai)
        print()

    def new_enemy_appear(self):
        print("Un nouvel ennemi apparait !")

    def take_damage(self):
        print(f"Outch ! Le {m.name} inflige ⚔️ {m.damage} dégâts.")
        print(f"Vous avez maintenant ❤️ {p.health} points de vie.")

    def player_dead(self):
        print("Vous êtes mort au combat.💀")

    # def clear_screen(self):
    #     if sys.platform.startswith('win'):
    #         os.system('cls')
    #     else:
    #         os.system('clear')

    # def clear_screen(self):
    #     print("\033c", end="")

    def separate_logic(self):
        print("═════════════════════════════════════════════════")

    def separate_elem(self):
        print("=================================================")