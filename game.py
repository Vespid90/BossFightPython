from player import Player
from enemy import Enemy

player = Player("Hero")
enemy = Enemy("Monster")
boss = Enemy("Boss")

def stats(pl, en):
    print("__________________________")
    print("Your stats \t\tEnemy stats")
    print("__________________________")
    print(f"Health: {pl.health}\t\tDamage(s): {en.damage}")
    print(f"Level: {pl.level}\t\tLevel: {en.level}")


class Game:
    def __init__(self, name):
        self.name = name

    def start_game(self):
        print("Welcome to our new RPG, BossFight! Are you ready to embark on an epic adventure?")
        e = enemy
        p = player
        while p.level <= 100:
            start = input("Enter 'a' to attack, 's' to show stats or 'l' to leave: ")
            if start == "a":
                stats(p, e)
                print("New enemy attacked")
                if e.enemy_level(p.level) <= p.level:
                    p.level_up()
                    p.health_up()
                    print("You killed the enemy ! \nYou leveled up !!")
                elif e.enemy_level(p.level) > p.level:
                    p.health_lose(e.attack())
                    print(f"Outch ! You take {e.attack()} damage(s)")
                elif p.health <= 0:
                    print("You lose this fight. Don't give up and restart!")
            elif start == "s":
                stats(p,e)
            elif start == "l":
                print("Thank you for playing ! See you soon !")
                quit()
            else:
                print("You need to choose between 'a', 's' or 'l' !")