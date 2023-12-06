from entities import Hero, Enemy
from weapon import Weapons
import curses
import random
from weapon import Fists, Rusted_Sword, Broken_Dagger, Conditioned_Blade, Skirmished_Scimitar, Oathkeeper, Spiked_Gauntlets, Defiler
import sys


player = Hero("Vigor", 155, constitution= 5, pots = 3)


def combat(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    enemy = encounter_enemy()

    key = 0
    while key != 27:
        stdscr.clear()

        display_stats(stdscr, player, enemy)

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('1'):
            player.attack(enemy)
            enemy.attack(player)


            display_stats(stdscr, player, enemy)

            stdscr.refresh()

            if player.health <= 0:
                stdscr.addstr(13, 0, "Your Journey end here. There is nothing you can do.")
                stdscr.refresh()
                sys.exit()

            if enemy.health <= 0:
                stdscr.addstr(10, 0, "You survived against the enemy")
                dropped = random.choice(weapons_list)
                if dropped == None:
                    stdscr.addstr(13, 0, "It left nothing")
                    stdscr.addstr(14, 0, "Press any key to continue...")
                else:
                    stdscr.addstr(13, 0, f"Amidst the mist, {dropped.name}")
                    stdscr.addstr(14, 0, "Press 3 to equip..")
                    stdscr.addstr(15, 0, "Or press any key twice to ignore..")

                    stdscr.refresh()
                    equip_key = stdscr.getch()

                    if equip_key == ord('3'):
                        player.weapon = dropped
                        stdscr.addstr(15, 0, f"You equipped the {dropped.name}")
                        stdscr.addstr(16, 0, "Press any key to continue...")
                        stdscr.refresh()
                    

                break

                

        if key == ord('2'):
            if player.hp_pot():
                player.hp_pot()
            else:
                 stdscr.addstr(13, 0, "You are out of health pots..")




        if key == ord('4'):
            if player.run():
                stdscr.addstr(13, 0, "You ran away from the enemy")
                stdscr.addstr(14, 0, "Press any key to continue...")
                break
            else:
                stdscr.addstr(13, 0, "You are out of stamina..")
    


        
    stdscr.getch()



def encounter_enemy():
    chance = random.randint(1, 70)
    if chance <= 10:
        return Enemy("Defiled Corpse",20, Weapons("Mucus Fingers", damage = random.randint(1, 10)))
    elif chance <= 20:
        return Enemy("Issacian", 35, Weapons("Solid Teardrop", damage = random.randint(10, 20)))
    elif chance <= 30:
        return Enemy("Slime Feces", 30, Weapons("Black Breath", damage = random.randint(20, 50)))
    elif chance <= 40:
        return Enemy("Corpse Siren", 30, Weapons("Membrane Screech", damage = random.randint(20, 50)))
    elif chance <= 50:
        return Enemy("Eyes for Teeth, Teeth for Eyes", 30, Weapons("Cavity Eyes", damage = random.randint(20, 50)))
    elif chance <= 60:
        return Enemy("Skeletal Mother", 30, Weapons("Deformed Fetus", damage = random.randint(20, 50)))
    elif chance <= 70:
        return Enemy("Muscled Weaponry", 30, Weapons("Splitstreaker", damage = random.randint(20, 50)))


def display_stats(stdscr, player, enemy):
    stdscr.clear()
    stdscr.addstr(7, 49, f" PLAYER STATS ",curses.A_REVERSE)
    stdscr.addstr(8, 45, f"  VIGOR: {player.health}", curses.A_BOLD)
    stdscr.addstr(9, 45, f"  CONSTITUTION: {player.stamina}", curses.A_BOLD)
    stdscr.addstr(10, 45, f"  WEAPON: {player.weapon.name}", curses.A_BOLD)
    stdscr.addstr(11, 45, f"  FLASK(s): {player.pots}", curses.A_BOLD)

    stdscr.addstr(8, 0, f"A {enemy.name} sees you.", curses.A_REVERSE)
    stdscr.addstr(9, 0, f"Vigor: {enemy.health}")
    stdscr.addstr(10, 0, f"MAGIK: {enemy.weapon.name}")
    stdscr.addstr(11, 0, f"DAMAGE: {enemy.weapon.damage}")

    stdscr.addstr(2, 0, "  '1': Slash                        ", curses.A_REVERSE)
    stdscr.addstr(3, 0, "  '2': Health Flask             ", curses.A_REVERSE)
    stdscr.addstr(4, 0, "  '3': Retrieve Weapons                ", curses.A_REVERSE)
    stdscr.addstr(5, 0, "  '4': Run          ", curses.A_REVERSE)
    stdscr.addstr(6,  0, "  'Spacebar': Retrieve Treasures      ", curses.A_REVERSE)
    stdscr.refresh()

weapons_list = [None, Rusted_Sword, Broken_Dagger, Conditioned_Blade, Skirmished_Scimitar, Oathkeeper, Spiked_Gauntlets, Defiler]



