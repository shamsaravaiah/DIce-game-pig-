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
    def make_move(self,opponent_score=None, my_score=None):
        decision = random.choice(['roll', 'hold'])
        return decision


class Computer_Player_Medium(Player):
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
            






class Computer_Player_Hard(Player):
    pass

