import random


class Player:
    def __init__(self, name):
        self.__name = name
        self.__score = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_score(self, score):
        self.__score += score 

    def get_score(self):
        return self.__score
    
    def make_move(self):
        pass
        
    def __str__(self) :

        return f"Name: {self.get_name()}, Score: {self.get_score()}"
    

class Human_Player(Player):
    def make_move(self):
        while True:
            move = input("Enter your move (q to quit, s to restart, h to hold, r to roll): ")
            if move == 'q':
                return 'quit'
            elif move == 's':
                return 'restart'
            elif move == 'h':
                return 'hold'
            elif move == 'r':
                return 'roll'
            else:
                print("Invalid move. Please try again.")



class Computer_Player_Easy(Player):
    def make_move(self,opponent_score=None, my_score=None, turn_total=None):
        decision = random.choice(['roll', 'hold'])
        return decision


class Computer_Player_Medium(Player):
    def make_move( opponent_score, my_score, turn_total):
        if turn_total >= 20:
            return 'hold'
        else:
            'roll'
        #Hold at 20' is a popular strategy. Each turn, the player rolls until they score 20 or more,
        #then holds. This strategy has an 8% disadvantage against optimal play.' into a function


        



class Computer_Player_Hard(Player):
    """use the End race or keep pace appraoch"""
    def make_move(self, opponent_score, my_score ):
        difference = abs(opponent_score - my_score)
        threshold = 21 + (difference / 8)
        if (my_score >= 71):
            return 'roll'
        elif my_score >= threshold:
            return 'hold'
        elif my_score <= threshold:
            return 'roll'
        else:
            return 'roll'
        #End race or keep pace'. If either player has a score of 71 or higher, roll to win. 
        #Otherwise, hold on 21 plus the difference between scores divided by 8. This has a 0.9% disadvantage against optimal play.
            






