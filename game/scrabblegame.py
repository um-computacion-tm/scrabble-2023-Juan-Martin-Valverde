from game.bagtiles import BagTiles
from game.player import Player
from game.board import Board
from game.dictionary import valid_word
from game.tiles import Tile


class InvalidWordException(Exception):
    pass
class InvalidPlaceWordException(Exception):
    pass
class InvalidWordNoLetters(Exception):
    pass

class ScrabbleGame():
    def __init__(self, total_players: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for index in range(total_players):
            self.players.append(Player(id=index, bag_tiles=self.bag_tiles))
        self.current_player = None
        self.round = 1
        self.score = []
        self.dict = valid_word() 
        

    def is_playing(self):
        if len(self.bag_tiles.total_tiles) > 0:
            return True
        else:
            return False


    def next_turn(self): 
        if self.current_player is None or self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]
        return self.current_player, self.round 
    
    def exchange_tiles(self, old_tiles_indices): #test
        player = self.current_player
        if all(1 <= i <= 7 for i in old_tiles_indices):
            old_tiles = []
            for i in old_tiles_indices:
                old_tiles.append(player.playertiles[i - 1])

            new_tiles = self.bag_tiles.take(len(old_tiles_indices))
            exchanged_tiles = []

            for i in old_tiles_indices:
                exchanged_tiles.append(player.playertiles[i - 1])
                player.playertiles[i - 1] = new_tiles.pop(0)

            self.bag_tiles.put(old_tiles)

            return exchanged_tiles
        else:
            print("Valor invalido de la letra. por favor ingresa un valor entre 1 y 7 (1 para tu primer letra 7 para tu ultima letra.")
            return []
    
    def exchange_all_tiles(self): 
        self.current_player
        all_tile_indx=list(range(1,8))
        exchanged_tiles = self.exchange_tiles(all_tile_indx)
        return exchanged_tiles
    

    def round_set(self):
        for player in self.players:
            while len(player.playertiles) < 7:
                remaining_tiles = 7 - len(player.playertiles)
                new_tiles = self.bag_tiles.take(remaining_tiles)
                player.playertiles.extend(new_tiles)
    
    def start_game(self): 
        return self.round_set()

    def validate_word(self, word, location, orientation): 
        if not self.current_player.has_letter(word):
            raise InvalidWordNoLetters("No tienes las letras necesaria para esta palabra.") 

        if not self.board.valid_word_in_board(word, location, orientation):
            raise InvalidPlaceWordException("La palabra se sale del tablero.")
        if not self.board.valid_word_in_place(word, location, orientation):
            raise InvalidPlaceWordException("Posicion no valida en el tablero.")

    def validate_word_first_round(self, word, location, orientation):
        if not self.current_player.has_letter(word):
            raise InvalidWordNoLetters("No tienes las letras necesaria para esta palabra.")
        if not self.dict.is_in_dictionary(word): 
            raise InvalidWordException("La palabra no existe.")
        if not self.board.valid_word_in_board(word, location, orientation):
            raise InvalidPlaceWordException("La palabra se sale del tablero.")
    
    def play_first_round(self, word, location, orientation): 
        self.board.put_first_word(word, location, orientation)            
        self.current_player.play_word(word)
        word_cells = self.board.get_word_cells(word, location, orientation) 
        total_score = self.board.calculate_word_value(word_cells)  
        self.current_player.score += total_score
        self.round += 1
        self.next_turn()

    def play(self, word, location, orientation): 
        self.board.put_word(word, location, orientation)            
        self.current_player.play_word(word)
        word_cells = self.board.get_word_cells(word, location, orientation)
        total_score = self.board.calculate_word_value(word_cells)
        self.current_player.score += total_score 
        self.next_turn() 

    
    def get_current_player(self): 
        return self.players[self.current_player.id]

    def player_has_comodin(self):
        current_player = self.get_current_player()
        return current_player.player_has_comodin()

    def change_comodin_to_tiles(self, letter):
        current_player = self.get_current_player()
        current_player.change_comodin_to_tiles(letter)

    def get_comodin_index(self):
        indice_comodin = [index for index, tile in enumerate(self.current_player.playertiles) if tile.letter == '?']
        if indice_comodin:
            return indice_comodin[0]
        else:
            raise ValueError("No esta el comodin entre tus letras.")
    
    def get_valid_letter_input(self):
        new_letter = input("Ingresa la letra que deseas que sea el comodin(en mayusculas): ").upper()
        if new_letter.isalpha() and len(new_letter) == 1 and new_letter.isupper():
            return new_letter
        else:
            raise ValueError("Entrada incorrecta, tiene que se en MAYUSCULAS para que sea valido.")
    
    def winner(self):
        max_score = max(player.score for player in self.players)
        winning_players = [player for player in self.players if player.score == max_score]
        
        return winning_players[0] if winning_players else None
    
    #//2/2