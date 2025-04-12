from player import Player
from enemy import Enemy
import time
import sys

player = Player("Hero")
enemy = Enemy("Monster")
# boss = Enemy("Boss")

def stats(pl, en):
    print("==========================================")
    print("Stats du Héro\t\tStats ennemi")
    print("==========================================")
    print(f"Nom: {pl.name}\t\t        Nom: {en.name}")
    print(f"Vie: {pl.health}\t\t        Dégâts: {en.attack()}")
    print(f"Niveau: {pl.level}\t\t    Niveau: {en.level}")
    print("==========================================")

def stats_player(pl):
    print("==========================================")
    print("Stats du Héro")
    print("==========================================")
    print(f"Nom: {pl.name}")
    print(f"Vie: {pl.health}")
    print(f"Niveau: {pl.level}")
    print("==========================================")

def stats_enemy(en):
    print("==========================================")
    print("Enemy stats")
    print("==========================================")
    print(f"Name: {en.name}")
    print(f"Damage(s): {en.attack()}")
    print(f"Level: {en.level}")
    print("==========================================")

def text_speed(texte, delai=0.01):
    for i in texte:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delai)
    print()


class Game:
    def __init__(self, name):
        self.name = name

    def start_game(self):
        # print("Welcome to our new RPG, BossFight! Are you ready to embark on an epic adventure?")
        text_speed("Les brumes du monde ancien s’épaississent... \nDans les ténèbres des montagnes d’Obsydor, des créatures oubliées s’éveillent...\nToi, humble aventurier, tu as entendu l’appel.\nTon voyage commence ici.")
        print("==========================================")
        text_speed("Bienvenue dans l'univers de BossFight !")
        print("==========================================")
        player.name = input("Quel est ton nom?: ")
        e = enemy
        p = player
        while p.level <= 100:
            start = input("Entrez: \n'a' pour attaquer, \n's' pour voir les statistiques du personnage \n'q' pour quitter le jeu: ")
            if start == "a":
                if e.enemy_level(p.level) < p.level:
                    print("Un nouvel ennemi apparait ! Attention, il attaque !")
                    stats(p,e)
                    print(f"Bien joué {p.name}, tu as tué le {e.name} ! \nTu as gagné un niveau !!")
                    p.level_up()
                    p.health_up()
                    continue
                elif e.enemy_level(p.level) > p.level:
                    print("New enemy attacked")
                    stats(p,e)
                    p.health_lose(e.damage)
                    print(f"Outch ! Le {e.name} inflige {e.damage} dégâts")
                    print(f"Tu as maintenant {p.health} points de vie")
                    continue
                elif p.health <= 0:
                    stats_player(p)
                    print("Tu es mort au combat ..")
                    quit()
                else:
                    print("Un nouvel ennemi apparait ! Attention, il attaque !")
                    stats(p, e)
                    print(f"Bien joué {p.name}, tu as tué le {e.name} ! \nTu as gagné un niveau !!")
                    p.level_up()
                    p.health_up()
                    continue
                    # stats(p,e)
                    # print("error")
            elif start == "s":
                stats_player(p)
            elif start == "q":
                print("Merci d'avoir joué ! A bientôt!")
                quit()
            else:
                print("Vous devez choisir entre 'a', 's' ou 'q' !")