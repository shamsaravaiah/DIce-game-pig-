
import random
import pyfiglet
from colorama import Fore, Style
import time
import os

class Dice:

    def __init__(self):
        self.__dice_dict= {
            0: """\
            ┌─────────┐
            │ roll    │
            │  the    │
            │   dice !│
            └─────────┘""",
            1: """\
            ┌─────────┐
            │         │
            │    ●    │
            │         │
            └─────────┘""",
            2: """\
            ┌─────────┐
            │ ●       │
            │         │
            │       ● │
            └─────────┘""",
            3: """\
            ┌─────────┐
            │ ●       │
            │    ●    │
            │       ● │
            └─────────┘""",
            4: """\
            ┌─────────┐
            │ ●     ● │
            │         │
            │ ●     ● │
            └─────────┘""",
            5: """\
            ┌─────────┐
            │ ●     ● │
            │    ●    │
            │ ●     ● │
            └─────────┘""",
            6: """\
            ┌─────────┐
            │ ●     ● │
            │ ●     ● │
            │ ●     ● │
            └─────────┘"""
        }
    def roll_dice(self):
        return random.randint(1,6)

    def over_all_score(self, name, score):
        return(Fore.YELLOW + f"Name :{name} Score : {score}" + Style.RESET_ALL)  # Reset the color after printing



    def current_score(self, sum):
        
        return(Fore.YELLOW + f"{sum}" + Style.RESET_ALL)  # Reset the color after printing

    def get_dice(self):
        return self.__dice_dict

    
    def display(self, name, score, sum, num_dice):
        overall_score_str = self.over_all_score(name, score)
        current_score_str = (self.current_score(sum))
        print(overall_score_str)
        print()
        print(self.get_dice()[num_dice])
        print(f"you rolled a {num_dice}" if num_dice != 0 else "")
        print('current score :' + current_score_str)
        
    def rolling_animation(self):
        listy = list(self.__dice_dict.values())[1:]
        
        for _ in listy:

            print(_)
            time.sleep(0.15)
            os.system('clear')
    
        






        
    

 
