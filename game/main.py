from game.mainmenu import Main_Menu
from game.scrabblegame import ScrabbleGame  
def Begin_game(self):
    self.main_menu = Main_Menu() 
       
    self.main_menu.welcome_message()
    player_count = self.main_menu.get_player_count()
    self.scrabble = ScrabbleGame(total_players=player_count)

    while self.scrabble.is_playing():
        self.scrabble.next_turn()
        self.scrabble.start_game()

        while True:
            self.show_game_options()
            option = int(input("Elige tus opciones: "))
            self.handle_user_input(option)
 