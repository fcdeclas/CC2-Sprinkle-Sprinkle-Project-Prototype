import curses
import random
import sys
from entities import Hero
from weapon import Oathkeeper


player = Hero("YOU", 300, 5, 3)
player.equip(Oathkeeper)

class Boss:
    def __init__(self, health=500):
        self.health = health

    def attack(self, player):
        damage_dealt = random.randint(20, 50)
        player.health -= damage_dealt
        return damage_dealt

def draw_boss(stdscr):
    boss_ascii = """
  ________      .__  _____  _____.__  __  .__     
 /  _____/______|__|/ ____\/ ____\__|/  |_|  |__  
/   \  __\_  __ \  \   __\\   __\|  \   __\  |  \ 
\    \_\  \  | \/  ||  |   |  |  |  ||  | |   Y  |
 \______  /__|  |__||__|   |__|  |__||__| |___|  /
        \/                                     \/ 
    """
    stdscr.addstr(0, 0, boss_ascii)
def draw_stats(stdscr, player, boss):
    stdscr.addstr(7, 49, f" PLAYER STATS ",curses.A_REVERSE)
    stdscr.addstr(8, 45, f"  Vigor: {player.health}", curses.A_BOLD)
    stdscr.addstr(9, 45, f"  Constitution: {player.stamina}", curses.A_BOLD)
    stdscr.addstr(10, 45, f"  WEAPON: {player.weapon.name}", curses.A_BOLD)
    stdscr.addstr(11, 45, f"  Flasks: {player.pots}", curses.A_BOLD)

    stdscr.addstr(13, 0, f"Boss Health: {boss.health}")

def boss_fight(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    boss = Boss()

    while True:
        stdscr.clear()

        draw_boss(stdscr)
        draw_stats(stdscr, player, boss)

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('1'):
            player_damage = player.attack(boss)
            boss_damage = boss.attack(player)

            stdscr.addstr(15, 0, f"You dealt {player_damage} damage to the Absolute")
            stdscr.addstr(16, 0, f"The Absolute dealt {boss_damage} damage to you.")

            if player.health <= 0:
                stdscr.addstr(18, 0, "You are but another Legend.")
                sys.exit()

            if boss.health <= 0:
                stdscr.addstr(18, 0, "You have brought Victory to Humanity.")
                sys.exit()

        stdscr.refresh()
