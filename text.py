import time
import sys


class Interface:
    def __init__(self):
        self.name = "Interface"

    @staticmethod
    def separate_logic():
        print("═════════════════════════════════════════════════")

    @staticmethod
    def separate_elem():
        print("=================================================")

    @staticmethod
    def logo():
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


class TextDialogue:
    def __init__(self):
        self.name = "dialogue system"

    @staticmethod
    def text_speed(texte, delai=0.01):
        for i in texte:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(delai)
        print()

    @staticmethod
    def title_speed(texte, delai=0.002):
        for i in texte:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(delai)
        print()

    @staticmethod
    def intro():
        return "Les brumes du monde ancien s’épaississent... \nDans les ténèbres de la forêt d’Obsydor, des créatures oubliées s’éveillent...\nVous, humble aventurier, vous avez entendu l’appel.\nVotre voyage commence ici."

    @staticmethod
    def player_name():
        return input("Quel est votre nom?: \n")

    @staticmethod
    def game_menu():
        return input("Quelle action souhaitez-vous faire ?: \n'a' pour avancer dans la forêt, \n's' pour voir les statistiques du personnage \n'q' pour quitter la fôret d'Obsydor: \n")

    @staticmethod
    def power(player_name):
        return f"Je sens un grand pouvoir émaner de vous, {player_name}....\nBienvenue dans l'univers de BossFight !"

    @staticmethod
    def go_wood():
        return "Vous avancez dans la forêt..."



class TextFight:
    def __init__(self):
        self.name = "figting system"

    @staticmethod
    def new_enemy_appear():
         print("Un nouvel ennemi apparait !")

    @staticmethod
    def e_killed(player_name, monster_name):
        print(f"Bien joué {player_name}, vous avez tué le {monster_name} ! \nVous avez gagné un niveau 🆙!")

    @staticmethod
    def lvl_up(player_lvl, player_health):
        print(f"Vous êtes maintenant niveau ⬆️ {player_lvl} et vous avez {player_health} ❤️ points de vie.")

    @staticmethod
    def take_damage(monster_name, monster_damage, player_health):
        print(f"Outch ! Le {monster_name} inflige ⚔️ {monster_damage} dégâts.")
        print(f"Vous avez maintenant ❤️ {player_health} points de vie.")

    @staticmethod
    def trap_damages(player_health_lose, player_health):
        print(f"Vous êtes tombé sur un piège ! vous perdez {player_health_lose} points de vie.")
        print(f"Vous avez maintenant {player_health} ❤️ points de vie.")

    @staticmethod
    def walk_damage(player_health_lose,player_health):
        print(f"Vous vous blessez en marchant ! Vous perdez {player_health_lose} point de vie.")
        print(f"Vous avez maintenant {player_health} ❤️ points de vie.")

    @staticmethod
    def p_dead():
        print("Vous êtes mort au combat.💀")


class TextItem:
    def __init__(self):
        self.name = "item system"

    @staticmethod
    def obj():
        return ["Explose", "Potion de soin", "Collier de soin", "Epée", "Bouclier", "Casque", "Armure", "Jambière", "Botte", "Gants", "Brassard", "Bombe"]

    @staticmethod
    def go_search():
        return "Vous fouillez les alentours..."

    @staticmethod
    def healing_pot(item, player_health):
        print(f"Vous avez trouvé une {item}.")
        print(f"Vous avez maintenant ❤️ {player_health} point(s) de vie.")

    @staticmethod
    def healing_neck(item, player_health):
        print(f"Vous avez trouvé un {item}.")
        print(f"Vous avez maintenant ❤️ {player_health} point(s) de vie.")