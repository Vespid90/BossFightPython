# from game import monster
# from game import player
# from stats import Stats
import random
import time
import sys
import os

# stats = Stats()
# m = monster
# p = player

class Text():
    def __init__(self):
        self.name = "text"

    def intro(self):
        return "Les brumes du monde ancien s’épaississent... \nDans les ténèbres de la forêt d’Obsydor, des créatures oubliées s’éveillent...\nVous, humble aventurier, vous avez entendu l’appel.\nVotre voyage commence ici."
    def game_menu(self):
        return input("Quelle action souhaitez-vous faire ?: \n'a' pour avancer dans la forêt, \n's' pour voir les statistiques du personnage \n'q' pour quitter la fôret d'Obsydor: \n")

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

    def power(self, player_name):
        return f"Je sens un grand pouvoir émaner de vous, {player_name}....\nBienvenue dans l'univers de BossFight !"

    def new_enemy_appear(self):
         print("Un nouvel ennemi apparait !")

    def e_killed(self, player_name, monster_name):
        print(f"Bien joué {player_name}, vous avez tué le {monster_name} ! \nVous avez gagné un niveau 🆙!")

    def lvl_up(self, player_lvl, player_health):
        print(f"Vous êtes maintenant niveau ⬆️ {player_lvl} et vous avez {player_health} ❤️ points de vie.")

    def take_damage(self, monster_name, monster_damage, player_health):
        print(f"Outch ! Le {monster_name} inflige ⚔️ {monster_damage} dégâts.")
        print(f"Vous avez maintenant ❤️ {player_health} points de vie.")

    def trap_damages(self, player_health):
        print(f"Vous êtes tombé sur un piège ! vous perdez 3 points de vie.")
        print(f"Vous avez maintenant {player_health} ❤️ points de vie.")

    def p_dead(self):
        print("Vous êtes mort au combat.💀")

    def separate_logic(self):
        print("═════════════════════════════════════════════════")

    def separate_elem(self):
        print("=================================================")

    def logo(self):
        return """
                        ______                _______        _     _
                        | ___ \               |  ___(_)     | |   | |
                        | |_/ / ___  ___ ___  | |_   _  __ _| |__ | |_
                        | ___ \/ _ \/ __/ __| |  _| | |/ _` | '_ \| __|
                        | |_/ / (_) \__ \__ \ | |   | | (_| | | | | |_
                        \____/ \___/|___/___/ \_|   |_|\__, |_| |_|\__|
                                                        __/ |
                                                       |___/
                             /   ))     |\         )               ).
                       c--. (\  ( `.    / )  (\   ( `.     ).     ( (
                       | |   ))  ) )   ( (   `.`.  ) )    ( (      ) )
                       | |  ( ( / _..----.._  ) | ( ( _..----.._  ( (
         ,-.           | |---) V.'-------.. `-. )-/.-' ..------ `--) \._
         | /===========| |  (   |      ) ( ``-.`\/'.-''           (   ) ``-._
         | | / / / / / | |--------------------->  <-------------------------_>=-
         | \===========| |                 ..-'./\.`-..                _,,-'
         `-'           | |-------._------''_.-'----`-._``------_.-----'
                       | |         ``----''            ``----''
                       | |
                       c--`                                                   """