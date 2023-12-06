import time
import os
import sys

def prompt():
    print("---------------------------------------")
    print("""
  ___                                  ___ ___                          .___
|    |    __ ________  __ __  ______  /   |   \  ____  __ __  ____    __| _/
|    |   |  |  \____ \|  |  \/  ___/ /    ~    \/  _ \|  |  \/    \  / __ | 
|    |___|  |  /  |_> >  |  /\___ \  \    Y    (  <_> )  |  /   |  \/ /_/ | 
|_______ \____/|   __/|____//____  >  \___|_  / \____/|____/|___|  /\____ | 
        \/     |__|              \/         \/                   \/      \/""")
    print("---------------------------------------")
    print(" input 'play' 'credits' 'exit'         ") 
    print("---------------------------------------")
    option = ""
    while option not in ['play', 'credits', 'exit']: 
        option = input("> ").lower()
        if option == 'play':
            introduction()
        elif option == 'credits':
            print("""Created by: 
                  Gian Cyrus F. Salvador
                  Fredmar Declas
                  Doniele Arys Antonio
                  Claudio Van Likigan
                  """)
            input("Enter to continue")
            os.system("cls")
            prompt()

        elif option == 'exit':
            sys.exit()
        else:
            print("Please input valid command('start' or 'quit')")
            
def introduction():
    print("-----------------------------------------------")
    print("        The Journey shall never end            ")
    print("-----------------------------------------------")
    press_any_key_to_continue
    os.system('cls')
 
    introduction = """From where the world suffered from the All-Fathering, To where the cities bleak in fear with no restraint from the demon lord. One must understand that the journey
    you will venture will not leave you in a satisfactory path but rather a harsh place to be in. Venture the misty forests and avoid the hallucinations that you will seek in between
    try and conquer to achieve victory to your already fallen lands by the hands of the demon lord."""

    print_text_slowly(introduction)
    press_any_key_to_continue()
    os.system('cls')

    character_name = input(print_text_slowly("What is your characters name:"))
    print_text_slowly(f"Now {character_name}!, Tread Carefully in your journey.")
    press_any_key_to_continue()
    os.system('cls')

    instructions = f"""You will enter the misty forests of the All-Fathering, {character_name} Wonder the forests and reach him to where he lies dormant. unmoving and Unchanging.
    Till the both of you meet you will be bewildered."""
    print_text_slowly(instructions)
    press_any_key_to_continue()
    os.system('cls')

def print_text_slowly(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    return "> "

def press_any_key_to_continue():
    input("Press Enter to continue...")