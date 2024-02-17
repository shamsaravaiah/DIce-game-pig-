
from player import Player
from dice import Dice
from game import Game
from display import *
import sys

def main():
    print(dipslay_intro())
    user_input = input("Enter your choice ->")
    if user_input in ('1','2','3'):
        if user_input == '1':
            pass
        elif user_input == '2':
            player1=Player('bereket')
            player2=Player('sham')
            game1=Game(player1,player2)
            game1.startGame()
        else:
            print(dipslay_outro())
            sys.exit(0)
    else:
        pass
    

if __name__ == '__main__':
    main()

 