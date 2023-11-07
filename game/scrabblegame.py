from game.bagtiles import BagTiles
from game.player import Player
from game.board import Board
from game.dictionary import valid_word

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

    def is_playing(self):
        if len(self.bag_tiles.total_tiles) > 0:
            return True
        else:
            raise False

    def next_turn(self): 
        self.round += 1
        if self.current_player is None or self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]
        return self.current_player, self.round 
    
    def exchange_tiles(self, old_tiles_indices):
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
            print("Indice de letra invalido. Por favor ingresa un numero entre 1 y 7 (1 para tu primer tile y 7 para tu ultima tile.")
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
            raise InvalidWordNoLetters("no tienes las letras necesarias para formar esta palabra")   
        if not self.board.valid_word_in_board(word, location, orientation):
            raise InvalidPlaceWordException("Tu palabra exede el tamaño del tablero")
        if not self.board.valid_word_in_place(word, location, orientation):
            raise InvalidPlaceWordException("No es una posicion valida en el tablero")
    
    def validate_word_fist_round(self, word, location, orientation):
        if not self.current_player.has_letter(word):
            raise InvalidWordNoLetters("no tienes las letras para formar esta palabra")
        if not self.board.valid_word_in_board(word, location, orientation):
            raise InvalidPlaceWordException("Tu palabra exede el tamaño del tablero")
        self.board.put_first_word(word, location, orientation)

    
    def play_first_round(self, word, location, orientation):
        if not self.validate_word_fist_round(word, location, orientation):
            self.current_player.play_word(word)
            self.board.put_word(word, location, orientation)

    def play(self,word,location,orientation):
        if not self.validate_word(word, location, orientation):
            self.current_player.play_word(word)
            self.board.put_word(word,location,orientation)

        return self.current_player.score

    
    def get_current_player(self) -> Player:
        return self.players[self.current_player.id]