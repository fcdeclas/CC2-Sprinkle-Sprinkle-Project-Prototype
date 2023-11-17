import sys,time,random,os

#typing speed (use if theres dialogue.) 
typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*8.0/typing_speed)
    print ('') #Be sure to use slow_type("") if you want to slow down the text

typing_speed = 50 #wpm
def EXTRA_slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*15.0/typing_speed)
    print ('') #Be sure to use slow_type("") if you want to slow down the text

def menu():
    print("[1] Start")
    print("[2] Credits")
    print("[0] Quit")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option ==1:
        slow_type("Starting the Game")
        slow_type("........")
        slow_type(".......")
        EXTRA_slow_type("At the Year 776, ")
        slow_type("The 5 Heroes blessed by the All-Fathering parted on the journey of Defeating The Lich that plagued Yarlo.")
        slow_type("Saving people along the way and Vanquishing the pointless wars that came to place.")
        slow_type("They arrived within the hallways where The Lich resided. The Hero 'Alexandr Holix' vowed to seal The Lich within the Amulet of Chavis.")
        slow_type("Honestly this is all for now for the intro")
        EXTRA_slow_type("That's all")
        print("")
        print("")
        input("Press Enter to Continue")
        os.system('cls')

        print()
        menu()
        option = int(input("Enter your option: "))

    elif option ==2:
        slow_type("Antonio, Declas, Likigan, Salvador")
        print("")
        print("")
        input("Press Enter to Continue")
        os.system('cls')
        
        print()
        menu()
        option = int(input("Enter your option: "))
    else:
        slow_type("You hear a voice in your head saying 'READ THE INSTRUCTIONS' in a calm tone ")
        print("")
        print("")
        input("Press Enter to Continue")
        os.system('cls')

        print()
        menu()
        option = int(input("Enter your option"))

slow_type("Edi goodbye")
input("Press Enter to Continue")
sys.exit()
    
