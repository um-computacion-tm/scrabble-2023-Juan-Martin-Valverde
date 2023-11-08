from game.mainmenu import Main_Menu
from game.scrabblegame import ScrabbleGame  

def Begin_game():
    main_menu = Main_Menu() 
       
    main_menu.welcome_message()
    player_count = main_menu.get_player_count()
    scrabble = ScrabbleGame(total_players=player_count)

    while scrabble.is_playing():
        scrabble.next_turn()
        scrabble.start_game()

        while True:
            main_menu.show_game_options()
            option = int(input("Elige tus opciones: "))
            main_menu.handle_user_input(option)
 
 #/2/2