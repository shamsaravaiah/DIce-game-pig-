from display import display_intro, display_rules, display_controls, choose_difficulty
import sys
from game_setup import single_player_game_setup, multi_player_game_setup

def user_interface():
    #display_intro()
    #display_rules()
    bool_val, user_input = display_controls()
    if bool_val:
        
        if user_input == '1': #single player
            player1 = 'bereket'
            single_player_game_setup(choose_difficulty(), player1)
        else: #multi player

            player1 = 'bereket'
            player2 = 'sham'
            multi_player_game_setup(player1, player2)
    
    else:
        # print(display_outro())
        # sys.exit(0)
        print('you quit')
