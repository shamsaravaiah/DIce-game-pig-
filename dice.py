
import random
import pyfiglet
import pyfiglet
from colorama import Fore, Style

class Dice:

    def __init__(self):
        self.__dice_dict= {
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
        print('current score :' + current_score_str)


    
        







        
    

 
