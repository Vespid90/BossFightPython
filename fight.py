from character import Player
from character import Monster
from text import Interface, TextFight
from stats import Stats
import random

p = Player("Hero")
m = Monster("Monster")
# # boss = Boss("Boss")

class Fight:
    def __init__(self):
        self.name = "Fight"

    @staticmethod
    def fight():
        alea = random.randint(0, 0)
        #======== nouvelle logic de combat ======#
        if alea == 0:
            TextFight.new_enemy_appear()
            lvl_enemy = m.monster_level(p.level)
            if lvl_enemy > p.level:
                Stats.stats(p, m)
                p.health_lose(m.damage)
                m.health_lose(p.damage)
                while p.health <= 0 or m.health <= 0:
                    p.health_lose(m.damage)
                    m.health_lose(p.damage)
                    TextFight.take_damage(m.name, m.damage, p.health)
                    Interface.separate_logic()
                    if p.health <= 0:
                        TextFight.p_dead()
                        Stats.stats_player(p)
                        quit()
                    else:
                        # elif m.health <= 0:
                        TextFight.e_killed(p.name, m.name)
                        p.level_up()
                        TextFight.lvl_up(p.level, p.health)
                        Interface.separate_logic()
                        continue
                    # else:
                    #     continue
            elif lvl_enemy <= p.level:
                Stats.stats(p, m)
                m.health_lose(p.damage)
                p.health_lose(m.damage)
                while p.health <= 0 or m.health <= 0:
                    m.health_lose(p.damage)
                    p.health_lose(m.damage)
                    TextFight.take_damage(m.name, m.damage, p.health)
                    Interface.separate_logic()
                    if p.health <= 0:
                        TextFight.p_dead()
                        Stats.stats_player(p)
                        quit()
                    # elif m.health <= 0:
                    else:
                        TextFight.e_killed(p.name, m.name)
                        p.level_up()
                        TextFight.lvl_up(p.level, p.health)
                        Interface.separate_logic()
                        continue
                # Text.e_killed(p.name, m.name)
                # p.level_up()
                # Text.lvl_up(p.level, p.health)
                # Interface.separate_logic()
                # continue
            else:
                Stats.stats(p, m)
                print("error")