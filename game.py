from player import Player
from enemy import Enemy

player = Player("Hero")
enemy = Enemy("Monster")
boss = Enemy("Boss")

def stats(pl, en):
    print("__________________________")
    print("Your stats\t\tEnemy stats")
    print("__________________________")
    print(f"Health: {pl.health}\t\t Damage(s): {en.attack()}")
    print(f"Level: {pl.level}\t\tLevel: {en.level}")
    print("__________________________")

def stats_player(pl):
    print("__________________________")
    print("Your stats")
    print("__________________________")
    print(f"Health: {pl.health}")
    print(f"Level: {pl.level}")
    print("__________________________")

def stats_enemy(en):
    print("__________________________")
    print("Enemy stats")
    print("__________________________")
    print(f"Damage(s): {en.attack()}")
    print(f"Level: {en.level}")
    print("__________________________")


class Game:
    def __init__(self, name):
        self.name = name

    def start_game(self):
        print("Welcome to our new RPG, BossFight! Are you ready to embark on an epic adventure?")
        e = enemy
        p = player
        while p.level <= 100:
            start = input("Enter 'a' to attack, 's' to show stats or 'q' to quit the game: ")
            if start == "a":
                print("New enemy attacked")
                if e.enemy_level(p.level) <= p.level:
                    stats(p,e)
                    print("You killed the enemy ! \nYou leveled up !!")
                    p.level_up()
                    p.health_up()
                elif e.enemy_level(p.level) > p.level:
                    stats(p,e)
                    p.health_lose(e.damage)
                    print(f"Outch ! You take {e.damage} damage(s)")
                    print(f"Your life point is now at {p.health} hp")
                elif p.health <= 0:
                    stats_player(p)
                    print("You lose this fight. Don't give up and restart!")
            elif start == "s":
                stats_player(p)
            elif start == "q":
                print("Thank you for playing ! See you soon !")
                quit()
            else:
                print("You need to choose between 'a', 's' or 'q' !")