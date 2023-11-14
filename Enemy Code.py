#Enemy Classes

import random


class slime (object):
    name = "Slime"
    health = 20
    strength = 2
    defence = 2
    loot = random.randint (0,10)

class goblin (object):
    name = "Goblin"
    health = 25
    strength = 5
    defence = 5
    loot = random.randint(0,10)

class troll (object):
    name = "Troll"
    health = 50
    strength = 10
    defence = 3
    loot = random.randint(0,10)

class dragon(object):
    name = "Dragon"
    health = 200
    strength = 50
    defence = 50
    
def enemyselect(goblin,bat,troll):
    enemyList = [goblin,bat,troll]
    chance = random.randint(0,10)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["potion", "sword", "shield"]
    lootChance = random.randint(0,5)
    lootDrop = loot[lootChance]
    return lootDrop

def lootEffect(lootDrop, character):
    if lootDrop == "potion":
        character.health = character.health + 20
        print ("you drink the potion, increasing your health by 20!")
        print ("Your health is now", character.health)
        return character

    elif lootDrop == "sword":
        character.strength = character.strength + 2
        print ("you swap your sword for the newer, much sharper one!")
        print ("Your strength has been increased by 2")
        print ("your new strength is now", character.strength)
        return character

    elif lootDrop == "shield":
        character.defence = character.defence + 2
        print ("you swap your shield for the newer, much stronger one!")
        print ("Your defence has been increased by 2")
        print ("your new strength is now", character.defence)
        return character
