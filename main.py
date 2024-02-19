
from player import Human_Player, Computer_Player
from game import Game
from display import dipslay_intro, dipslay_outro
import sys

def main():
    difficulty_level = ('1','2','3')
    print(dipslay_intro())
    user_input = input("Enter your choice ->")
    if user_input in ('1', '2', '3'):
        if user_input == '1':
            user_difficulty = input("\nChoose Difficulty level:- \n 1. Easy \n 2. Medium \n 3. Hard \n ->")
            if user_difficulty in difficulty_level:
                if user_difficulty == '1':
                    player1 = Human_Player('bereket')
                    player2 = Computer_Player('Souxie')
                    single_player_game = Game(player1, player2)
                    single_player_game.Start_Game()
                    pass
                elif user_difficulty == '2':
                    pass
                else:
                    pass

            else: 
                pass
        elif user_input == '2':
            player1 = Human_Player('bereket')
            player2 = Human_Player('sham')
            multiplayer_game = Game(player1, player2)
            multiplayer_game.Start_Game()
        else:
            print(dipslay_outro())
            sys.exit(0)
    else:
        pass


if __name__ == '__main__':
    main()