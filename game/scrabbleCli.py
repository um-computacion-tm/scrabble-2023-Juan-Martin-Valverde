from game.scrabblegame import ScrabbleGame

class ScrabbleCli:
    
    def __init__(self):
        self.scrabble = None

    def welcome_message(self):
        print("--------------------------------------------------------------------------------------------")
        print("---------------------------------------Welcome to Scrabble----------------------------------")
        print("--------------------------------------------------------------------------------------------")

    def get_player_count(self):
        while True:
            try:
                player_count = int(input("Enter the number of Players (2-4): "))
                if player_count >= 2 and player_count <= 4:
                    return player_count
                else:
                    print("Invalid number of players. Please enter a number between 2 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def show_game_options(self):
        print("----------------------------------------Scrabble Board-----------------------------------------")
        print(self.scrabble.board)
        print("-------------------------------------------Options---------------------------------------------")
        print("Press 1 to Put Word")
        print("Press 2 to Change your Tiles")
        print("Press 3 to Change all your Tiles")
        print("Press 4 to Pass Turn")
        print("Press 5 to End the Game")
        print("Press 6 to Convert Joker")
        print("-----------------------------------------------------------------------------------------------")
        print(self.scrabble.get_current_player())

    def get_word_input(self):
        while True:
            word = input("Enter your Word: ").upper()
            if word.isalpha():
                return word
            else:
                print("Invalid word. Please enter alphabetic characters only.")

    def get_coordinates(self):
        while True:
            try:
                x = int(input("Enter your Word pos Row: "))
                y = int(input("Enter your Word pos Col: "))
                return (x, y)
            except ValueError:
                print("Invalid input. Please enter valid numbers for coordinates.")

    def get_orientation(self):
        while True:
            orientation = input("Enter the Word orientation (H/V): ").upper()
            if orientation in ['H', 'V']:
                return orientation
            else:
                print("Invalid orientation. Please enter 'H' for horizontal or 'V' for vertical.")

    def handle_user_input(self, option):
      try: 
          if option == 1:
              word = self.get_word_input()
              location = self.get_coordinates()
              orientation = self.get_orientation()
              if self.scrabble.round < 2:
                  self.scrabble.validate_word_first_round(word, location, orientation)
                  self.scrabble.play_first_round(word, location, orientation)
                  self.scrabble.round_set()
              else:
                  self.scrabble.validate_word(word, location, orientation)
                  self.scrabble.play(word, location, orientation)
                  self.scrabble.round_set()
          elif option == 2:
              self.handle_option_2()
          elif option == 3:
              self.handle_option_3()
          elif option == 4:
              self.handle_option_4()
          elif option == 5:
              self.handle_option_5()
          elif option == 6:
              self.handle_option_6()
          else:
              print("Incorrect Input. Please try again.")

      except ValueError as e:
          print(f"Error: {e}. Please enter a valid input.")

    def handle_option_2(self):
        tiles_to_exchange_indices = input("Enter the indices of tiles you want to exchange (comma-separated): ").split(',')
        old_tiles_indices = [int(index.strip()) for index in tiles_to_exchange_indices]
        exchanged_tiles = self.scrabble.exchange_tiles(old_tiles_indices)
        print("Exchanged tiles: ", exchanged_tiles)
        self.scrabble.next_turn()

    def handle_option_3(self):
        print('Okay, exchanging all your tiles')
        exchanged_tiles = self.scrabble.exchange_all_tiles()
        print("Exchanged tiles: ", exchanged_tiles)
        self.scrabble.next_turn()

    def handle_option_4(self):
        print("Well, passing to the next player...")
        self.scrabble.next_turn()

    def handle_option_5(self):
        winner = self.scrabble.winner()
        print(f"The winner is Player: {winner.id}, with a score of {winner.score}")
        print("Thanks for playing, bye...")
        exit()

    def handle_option_6(self):
        if self.scrabble.current_player.has_joker():
            self.scrabble.get_joker_index()
            new_letter = self.scrabble.get_valid_letter_input()
            self.scrabble.convert_joker_to_letter(new_letter)
        else:
            raise Exception("Player does not have a Joker in their tiles.")

    def client(self):
        self.welcome_message()
        player_count = self.get_player_count()
        self.scrabble = ScrabbleGame(total_players=player_count)

        while self.scrabble.is_playing():
            self.scrabble.next_turn()
            self.scrabble.start_game()

            while True:
                self.show_game_options()
                try:
                    option = int(input("Choose your Option: "))
                    self.handle_user_input(option)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                except Exception as e:
                    print(f"Error: {e}. Please try again.")


