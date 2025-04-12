from player import Player
from enemy import Enemy
import time
import sys

player = Player("Hero")
enemy = Enemy("Monster")
# boss = Enemy("Boss")

def stats(pl, en):
    print("==========================================")
    print(f"{'Stats du Héro':<26}{'Stats ennemi':<20}")
    print("==========================================")
    print(f"Nom: {pl.name:<20} Nom: {en.name:<20}")
    print(f"Vie: {pl.health:<20} Dégâts: {en.attack():<20}")
    print(f"Niveau: {pl.level:<17} Niveau: {en.level:<20}")
    print("==========================================")


def stats_player(pl):
    print("==========================================")
    print("Stats du Héro")
    print("==========================================")
    print(f"Nom: {pl.name}")
    print(f"Vie: {pl.health}")
    print(f"Niveau: {pl.level}")
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
        text_speed("Les brumes du monde ancien s’épaississent... \nDans les ténèbres de la forêt d’Obsydor, des créatures oubliées s’éveillent...\nToi, humble aventurier, tu as entendu l’appel.\nTon voyage commence ici.")
        print("==========================================")
        text_speed("Bienvenue dans l'univers de BossFight !")
        print("==========================================")
        player.name = input("Quel est ton nom?: \n")
        e = enemy
        p = player
        while p.level <= 100:
            start = input("Entrez: \n'a' pour avancer dans la forêt, \n's' pour voir les statistiques du personnage \n'q' pour quitter l'ancien monde: \n")
            if start == "a":
                if e.enemy_level(p.level) < p.level:
                    print("Un nouvel ennemi apparait ! Attention, il attaque !")
                    stats(p,e)
                    print(f"Bien joué {p.name}, tu as tué le {e.name} ! \nTu as gagné un niveau !!")
                    print("==========================================")
                    p.level_up()
                    p.health_up()
                    continue
                elif e.enemy_level(p.level) > p.level:
                    print("Un nouvel ennemi apparait !\nAttention, il attaque !")
                    stats(p,e)
                    p.health_lose(e.damage)
                    print(f"Outch ! Le {e.name} inflige {e.damage} dégâts")
                    print(f"Tu as maintenant {p.health} points de vie")
                    if p.health <= 0:
                        stats_player(p)
                        print("Tu es mort au combat ..")
                        print("==========================================")
                        quit()
                    else:
                        continue
                else:
                    print("Un nouvel ennemi apparait !\nAttention, il attaque !")
                    stats(p, e)
                    print(f"Bien joué {p.name}, tu as tué le {e.name} ! \nTu as gagné un niveau !!")
                    print("==========================================")
                    p.level_up()
                    p.health_up()
                    continue
            elif start == "s":
                stats_player(p)
            elif start == "q":
                print("Merci d'avoir joué ! A bientôt!")
                print("==========================================")
                quit()
            else:
                print("Vous devez choisir entre 'a', 's' ou 'q' !")
                print("==========================================")