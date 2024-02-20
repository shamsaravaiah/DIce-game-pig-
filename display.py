

import os
import time
import pyfiglet
from colorama import Fore, Style




def display_intro():
    os.system('clear')
    start_time = time.time()  # Record the start time
    duration = 2.2  # Duration of 3 seconds
    text = pyfiglet.figlet_format("P  I  G", font="big_money-se")
    color_codes = [getattr(Fore, color.upper(), Fore.WHITE) for color in ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]]
    while time.time() - start_time < duration:
        for color in color_codes:
            print(color + text + Style.RESET_ALL, end="\r", flush=True)
            time.sleep(0.3)
            os.system('clear')



def display_rules():
    os.system('clear')
    print(pyfiglet.figlet_format("RULES:", font="big_money-se"))
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
                The first player to reach the target score (e.g., 100) wins. All players may get one final turn to try to surpass the leading player's score in some variations.\n
        """)
    print(text)
    time.sleep(4)
    os.system('clear')
    
    
def display_controls():
    os.system('clear')
    

    print( pyfiglet.figlet_format("CONTROLS", font="big_money-se"))
    text = ("""
         
            - Press C at any point in the game to change your name\n
            - Press Q at any point in the game to Q\n
                
                1. Single player
                2. multiplayer
                3. Quit\n"""
    )

    print(text)
    user_input = input("Enter your choice ->")
    return user_input



def dipslay_outro():
    return  """
            THANK YOU FOR PLAYING THE DICE GAME (PIG)
            \n\n\n"""

 