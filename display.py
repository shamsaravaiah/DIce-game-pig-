

import os
import time
import pyfiglet
from colorama import Fore, Style
from check_platform import clear_command



def display_intro():
    os.system(clear_command)
    start_time = time.time()  # Record the start time
    duration = 2.2  # Duration of 3 seconds
    text = pyfiglet.figlet_format("P  I  G", font="big_money-se")
    color_codes = [getattr(Fore, color.upper(), Fore.WHITE) for color in ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]]
    while time.time() - start_time < duration:
        for color in color_codes:
            print(color + text + Style.RESET_ALL, end="\r", flush=True)
            time.sleep(0.3)
            os.system(clear_command)



def display_rules():
    os.system(clear_command)
    color = Fore.YELLOW  # For example, you can use Fore.RED for red text
    ascii_art = pyfiglet.figlet_format("RULES:", font="big_money-se")
    print(color + ascii_art + Style.RESET_ALL)  # Reset the color after printing

    text = ("""
        
    - Objective: Be the first to reach a certain point total, usually 100.\n
    - Players: Two or more.\n
    - Gameplay:\n
        Players take turns rolling a single die.\n
        On each turn, a player repeatedly rolls the die until they decide to "hold" or roll a 1.\n
    - Scoring:\n
        Rolling a 1 ends the turn with no points scored.\n
        Any other number adds to the player's turn total.\n
    - Holding: \n
        At any point during their turn, a player can choose to "hold", keeping all points accumulated.\n
    - Winning: \n
        The first player to reach the target score (e.g., 100) wins.
        """)
    print(text)
    time.sleep(5)
    os.system(clear_command)
    
    
def display_controls():
    os.system(clear_command)
    print( pyfiglet.figlet_format("CONTROLS", font="big_money-se"))
    text = ("""
         
            - Press C at any point in the game to change your name\n
            - Press Q at any point in the game to Q\n
                
            1. Single player\n
            2. multiplayer\n
            3. Quit\n"""
    )

    print(text)
    while True:
        user_input = input("Enter your choice -> ").strip()
        if user_input in ('1', '2', 'q'):
            if (user_input == '1') or (user_input == '2'):
                return True, user_input
            else: 
                return False, None

        else:
            print("Invalid input. Please enter 1, 2, q ")
    

def choose_difficulty():
    while True:
        user_difficulty = input("\nChoose Difficulty level:- \n\n 1. Easy \n\n 2. Medium \n\n 3. Hard \n\n ->").strip()
        if user_difficulty in ('1', '2', '3'):
            break  
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

    return user_difficulty




def dipslay_outro():
    return  """
            THANK YOU FOR PLAYING THE DICE GAME (PIG)
            \n\n\n"""



