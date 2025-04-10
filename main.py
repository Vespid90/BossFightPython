from player import Player
from enemy import Enemy

player = Player("Hero", 5, 1)
enemy = Enemy("Monster", 3, None)

def stats(pl, en):
    print("__________________________")
    print("Your stats \t\tEnemy stats")
    print("__________________________")
    print(f"Health: {pl.health}\t\tHealth: {en.health}")
    print(f"Level: {pl.level}\t\tLevel: {en.enemy_level(pl.level)}")

def start_game():
    print("Welcome to our new RPG, BossFight! Are you ready to embark on an epic adventure?")
    while player.level <= 10:
        start = input("Enter 1 to attack or 2 to leave: ")
        if start == "1":
                print("New enemy attacked")
                while True:
                    e = enemy
                    p = player
                    stats(p, e)
                    if e.enemy_level(p.level) <= p.level:
                        p.level_up()
                        p.health_up()
                        print("You killed the enemy ! \nYou leveled up !!")
                        break
                    elif e.enemy_level(p.level) > p.level:
                        p.health_lose()
                        print("Outch ! You take 1 damage")
                        break
                    elif p.health <= 0:
                        print("You lose this fight. Don't give up and restart!")
                        break
        elif start == "2":
            print("Thank you for playing ! See you soon !")
            quit()
        else:
            print("You need to choose between 1 or 2 !")

start_game()

