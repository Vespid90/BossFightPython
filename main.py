from player import Player
from enemy import Enemy

player = Player("Hero", 5, 1)
enemy = Enemy("Monster", 5)

def stats(p, en):
    print("__________________________")
    print("Your stats \t\tEnemy stats")
    print("__________________________")
    print(f"Health: {p.health}\t\tHealth: {en.health}")
    print(f"Level: {p.level}\t\tLevel: {en.enemy_level(p.level)}")


def enemy_death(en):
    enemies.remove(en)

enemies= [
    Enemy("Monster 1", 5),
    Enemy("Monster 2", 5),
    Enemy("Monster 3", 5),
]

while enemies:
    e = enemies[0]
    print("New enemy attacked")
    while True:
        attack = input("Enter 1 to attack: ")
        stats(player, enemy)
        if e.enemy_level(player.level) <= player.level:
            player.level += 1
            player.health += 2
            print("You killed the enemy ! \nYou leveled up !!")
            enemy_death(e)
            break
        elif e.enemy_level(player.level) > player.level:
            player.health_lose()
            print("Outch ! You take 1 damage")
            player.health -= 1
            break
        elif player.health <= 0:
            print("You lose this fight. Don't give up and restart!")
            print(player.level)
            break