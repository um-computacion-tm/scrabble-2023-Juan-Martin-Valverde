from game.tiles import Tile
from game.bagtiles import  BagTiles
class MissingTileInRackException(Exception):
    pass
class Player:
    MAX_PLAYERS = 4

    def __init__(self, player_id):
        if player_id is None or not isinstance(player_id, int):
            raise ValueError("Invalid player ID")
        self.player_id = player_id
        self.player_rack = []

    def __repr__(self):
        return f"Player(name={self.name}, player_rack={self.player_rack})"

    def play_word(self, word):
        for letter in word:
            if letter not in self.player_rack:
                raise ValueError("Tile not in player's rack")
            self.player_rack.remove(letter)
        return True

    def take_tiles(self, tiles):
        self.player_rack.extend(tiles)

    def exchange_tiles(self, bag, letters):
        replaced_tiles = []
        for letter in letters:
            for tile in self.player_rack:
                if tile == letter:
                    self.player_rack.remove(tile)
                    replaced_tiles.append(tile)
                    break

        new_tiles = bag.take(len(replaced_tiles))
        self.player_rack.extend(new_tiles)
        bag.put(replaced_tiles)
    
    def give_tiles(self, letters):
        rack_backup = self.player_rack.copy()
        tiles = []
        for i in range(len(letters)):
            letter_index = -1
            for j in range(7 - i):
                if j >= len(rack_backup):
                    break
                if rack_backup[j].letter == letters[i][0]:
                    letter_index = j
                    break
            if letter_index == -1:
                self.player_rack = rack_backup
                raise ValueError("Letter not in player's rack")
            tiles.append(rack_backup.pop(letter_index))
        return tiles
            
    def exchange_tiles(self, bag, letters):
        rack_backup = self.player_rack.copy()
        for letter in letters:
            if letter not in [tile.letter for tile in self.player_rack]:
                self.player_rack = rack_backup
                raise ValueError("Letter not in player's rack")
            self.player_rack.remove(next(tile for tile in self.player_rack if tile.letter == letter))
        self.player_rack += bag.take(len(letters))
        

    def get_player_id(self):
        return self.player_id

    def get_rack(self):
        return self.player_rack  
