from dice import Dice
import random
import time 
import os

class Game:
  
    def __init__(self,player1,player2,):
        self.player1=player1
        self.player2=player2

        self.current_player = [player1, player2]
    
    def roll_dice(self):
        return random.randint(1, 6)
        

    def startGame(self):
        gave_over = False
        player_index = 0
        sum=0
        while not gave_over:
            os.system('clear')
            if self.current_player[player_index].get_score() >=100:
                print(f"winner:{self.current_player[player_index].get_name} \nscore: {self.current_player[player_index].get_score()}")
                gave_over=True

            else:
                name = self.current_player[player_index].get_name()
                score = self.current_player[player_index].get_score()
                dice = Dice()
                num_dice=self.roll_dice()
                print(dice.over_all_score(name, score))
                print()
                print(dice.get_dice()[num_dice])
                print(dice.current_score(sum))
                
                if num_dice!=1:
                    sum+=num_dice
                    continue_var=input("Enter 'H' to hold and 'R' to roll again: ")
                    while continue_var.lower()  not in ('h','r'):
                        continue_var=input("Wrong input! Enter only 'H' to hold and 'R' to roll again: ")
                
                    if continue_var.lower() == "h":
                        self.current_player[player_index].set_score(sum)

                        sum=0
                        player_index = 1 - player_index
                    elif continue_var.lower() == 'r':
                        continue
                       
                            

                else:
                    print(f" YOU LOST {name}")
                    player_index = 1 - player_index 
            
        
                
                

          
                
          


    


    