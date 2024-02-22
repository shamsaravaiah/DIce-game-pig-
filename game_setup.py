from player import Human_Player, Computer_Player_Easy, Computer_Player_Medium, Computer_Player_Hard
from game import Game


def single_player_game_setup( user_difficulty, p1 ):
    
    player1 = Human_Player(p1)
    player2 = Computer_Player_Easy('Souxie') if user_difficulty == '1' else ( Computer_Player_Medium('Souxie') if user_difficulty == '2' else Computer_Player_Hard('Souxie') ) 
    single_player_game = Game(player1, player2)
    single_player_game.Start_Game()
    
    

def multi_player_game_setup(p1, p2):
    player1 = Human_Player(p1)
    player2 = Human_Player(p2)
    multiplayer_game = Game(player1, player2)
    multiplayer_game.Start_Game()