from dice import Dice
import os
from player import Human_Player
import time
import pyfiglet
from colorama import Fore, Style
from check_platform import clear_command

class Game:

    def __init__(self, player1, player2,):
        self.player1 = player1
        self.player2 = player2
        self.current_player = [player1, player2]

    
    def Start_Game(self):
        gave_over = False
        player_index = 0
        turn_total = 0
        continue_var = None # now its roll 
        clear = clear_command
        while not gave_over:
            os.system(clear)
            if self.current_player[player_index].get_score() >= 100:
                gave_over = True
                break
            else:
                name = self.current_player[player_index].get_name()
                score = self.current_player[player_index].get_score()
                dice = Dice()
                num_dice = dice.roll_dice()
                dice.display(name, score, turn_total, num_dice) #changed turn_total to 0
                if num_dice != 1:
                    if not isinstance(self.current_player[player_index], Human_Player): #ill explain this dont cry
                        turn_total += num_dice
                        continue_var = (self.current_player[player_index]).make_move(self.player1.get_score(), self.player2.get_score())
                        print(f'\nSouxie chose to {continue_var}')
                        time.sleep(1)
                        if continue_var == 'roll':
                            continue
                        else:
                            self.current_player[player_index].set_score(turn_total)
                            player_index = 1 - player_index
                            turn_total = 0               
                    else:
                        turn_total += num_dice
                        continue_var = self.current_player[player_index].make_move()     
                        if continue_var == 'quit':
                            print(f'{name} has left the game, with score -> {score}')
                            print(f'name : {self.current_player[0].get_name()}, score : {self.current_player[0].get_score()}')
                            print(f'name : {self.current_player[1].get_name()}, score : {self.current_player[1].get_score()}')
                            break
                        elif continue_var == 'restart':
                            pass
                        elif continue_var == 'hold':
                            turn_total = 0
                            self.current_player[player_index].set_score(turn_total)
                            player_index = 1 - player_index
                        else: #roll
                            continue
                else:
                    time.sleep(1)
                    os.system('clear')
                    player_index = 1 - player_index
                    color = Fore.RED  # For example, you can use Fore.RED for red text
                    ascii_art = pyfiglet.figlet_format(f"{name} ROLLED A 1", font="big_money-se")
                    print(color + ascii_art + Style.RESET_ALL)  # Reset the color after printing
                    time.sleep(2)
                    continue
            

        print(f"winner:{self.current_player[player_index].get_name()} \nscore: {self.current_player[player_index].get_score()}")
        

              