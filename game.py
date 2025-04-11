from player import Player
from enemy import Enemy

player = Player("Hero", 5, 1)
enemy = Enemy("Monster", 3)

def stats(pl, en):
    print("__________________________")
    print("Your stats \t\tEnemy stats")
    print("__________________________")
    print(f"Health: {pl.health}\t\tHealth: {en.health}")
    print(f"Level: {pl.level}\t\tLevel: {en.level}")

# monster = []

class Game:
    def __init__(self, name):
        self.name = name

    def start_game(self):
        print("Welcome to our new RPG, BossFight! Are you ready to embark on an epic adventure?")
        while player.level <= 100:
            start = input("Enter 1 to attack or 2 to leave: ")
            if start == "1":
                print("New enemy attacked")
                e = enemy
                p = player
                if e.enemy_level(p.level) <= p.level:
                    stats(player, enemy)
                    p.level_up()
                    p.health_up()
                    print("You killed the enemy ! \nYou leveled up !!")
                    continue
                elif e.enemy_level(p.level) > p.level:
                    stats(player, enemy)
                    p.health_lose()
                    print("Outch ! You take 1 damage")
                    continue
                elif p.health <= 0:
                    print("You lose this fight. Don't give up and restart!")
                    continue
            elif start == "2":
                print("Thank you for playing ! See you soon !")
                quit()
            else:
                print("You need to choose between 1 or 2 !")