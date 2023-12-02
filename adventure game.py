import sys,time,random,os

#typing speed (use if theres dialogue.) 
typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*6.0/typing_speed)
    print ('') #Be sure to use slow_type("") if you want to slow down the text

typing_speed = 50 #wpm
def EXTRA_slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*15.0/typing_speed)
    print ('') #Be sure to use slow_type("") if you want to slow down the text

EXTRA_slow_type("At the Year 776, ")
slow_type("The 5 Heroes blessed by the All-Fathering parted on the journey of Defeating The Lich that plagued Yarlo.")
slow_type("Saving people along the way and Vanquishing the pointless wars that came to place.")
slow_type("They arrived within the hallways where The Lich resided. The Hero 'Alexandr Holix' vowed to seal The Lich within the Amulet of Chavis.")
os.system('cls')

#Hero Classes
class rogue (object):
    health = 50
    strength = 10
    defence = 10
    magic = 1

class warlock (object):
    health = 125
    strength = 7
    defence = 7
    magic = 10

class hunter (object):
    health = 100
    strength = 5
    defence = 10
    magic = 7

# Enemy Classes

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
    
def gameOver(character, score):
    if character.health < 1:
        print("You have no health left")
        print("Thanks for playing...")
        print("You have scored...", score)
        
        writeScore(score)

        file=open("score.txt","r")

        for line in file:
            xline = line.split(",")
            print(xline[0], xline[1])

        exit()
        

def writeScore(score):
    file = open("score.txt","a")
    name = input("Type your name...")
    file.write(str(name))
    file.write(",")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()


def heroselect():
    print ("Select your hero!")
    selection = input("1. Rogue \n2. Warlock \n3. Hunter \n")
    if selection == "1":
        character = rogue
        print ("You have selected the rogue...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    elif selection == "2":
        character = warlock
        print ("You have selected the warlock...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    elif selection == "3":
        character = hunter
        print ("You have selected the hunter...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    else:
        print("Only press 1, 2 or 3")
        heroselect()

def enemyselect(slime,goblin,troll):
    enemyList = [goblin,slime,troll]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["potion", "sword", "shield"]
    lootChance = random.randint(0,2)
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

    
    
def battlestate(score):
    enemy = enemyselect(slime,goblin,troll)
    print("a wild", enemy.name, "has appeared!")
    print ("you have 3 options...")
    while enemy.health > 0 :
        choice = input("1. Sword\n2. Magic \n3. RUN!")

        if choice == "1":
            print ("You swing your sword, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print ("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 1:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)
                    

                else:
                    if enemy.name == "Slime":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Goblin":
                        enemy.health = 25
                        score = score + 5
                        

                    elif enemy.name == "Troll":
                        enemy.health = 50
                        score = score + 15
                        

                    print ("You have defeated the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("Your sword slips from your grasp, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "2":
            print ("You cast a spell, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.magic
                print ("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)

                else:
                    if enemy.name == "Slime":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Goblin":
                        enemy.health = 25
                        score = score + 5
                        

                    elif enemy.name == "Troll":
                        enemy.health = 50
                        score = score + 15
                        

                    print ("You have defeated the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("You slip when casting your spell, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "3":
            print("you try to run....")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("you got away unscratched!")
                break
            else:
                print ("You try to run but slip and fall")
                print ("You try to defend but cannot, the enemy hits you for full damage...")
                character.health = character.health - enemy.strength
                print ("Your health is now", character.health)
                gameOver(character, score)

        else:
            print ("number not allowed, please only type 1, 2 or 3...")
        

def BossBattleState(score, boss):
    enemy = boss
    



score = 0
character = heroselect()
score = battlestate(score)
print(score)
score = battlestate(score)
print(score)
score = battlestate(score)
print (score)
score = battlestate(score)
print(score)
score = battlestate(score)
print(score)
score = battlestate(score)
writeScore(score)
            
#Step Counter
player_steps = 0

#Dialogues
dialogue1 = ["I want to escape.", "When will this end?", "I want to give up.", "Please let all end.", "I don't want to continue this anymore",
            "I want to see my family again", "I don't want to die.", "I have a knife and it is not for my enemies."]
dialogue2 = ["Is a grave better than being tortured?", "What time of the day is it?", "I want to sleep.", "My bones are still intact. But my brain is not",
             "Will I ever see the light of day again?", "Maybe an eternal sleep will benefit me more."]
dialogue3 = ["Why did it not attack me?", "I'm a coward...", "Thank you God.", "I survived..?"]
dialogue_check_failed = ["Nothing seems to be of mind", "Your mental state slightly decreases", "Your mind is empty.", "Your mental state slightly increases"]

def player_move():
    print("Type w,a,s,d")
    if input.lower == ["w","a","s","d"]:
        player_steps += 1
    else:
        print("Are you retarded? Try again.")
        player_move()

if player_steps == 4:
    encounter = random.randint(0, 100)
    if encounter <= 50:
        slow_type(random.choice(dialogue1))

    else:
        slow_type(random.choice(dialogue_check_failed))

if player_steps == 5:
    encounter = random.randint(0, 100)
    if encounter <= 50:
        slow_type_EXTRA("An enemy found you.")
        os.system("cls")
        player_steps == 0 #Reset to 0

    else: 
        slow_type(random.choice(dialogue1))
        slow_type_EXTRA("You slowly become weary")

#Higher enemy encounter
if player_steps == 6:
    encounter = random.randint(0, 80)
    if encounter <= 40:
        slow_type_EXTRA("An enemy has found you.")
        player_steps == 0 #Reset again

    else: 
        slow_type(random.choice(dialogue1))
        slow_type_EXTRA("You slowly become weary")

#Safe reset.
if player_steps == 7:
    encounter <= random.randint(0, 50)
    if encounter <= random.randint <= 25:
        print("An enemy found you.")
        player_steps == 0 #reset

    else:
        slow_type(random.choice(dialogue2))
        slow_type(random.choice(dialogue3))
        player_steps == 0 #safe reset.
                
                


    



    
