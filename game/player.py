from game.tiles import Tile
from game.bagtiles import  BagTiles
class MissingTileInRackException(Exception):
    pass

class Player:
    def __init__(self, player_id= None, bag_tiles = BagTiles):
        
        self.player_id = player_id
        self.player_tiles = bag_tiles
        self.score = 0

    def get_player_id(self):
        return self.player_id
    
    def get_rack(self):
        return self.player_tiles

    def play_word(self, word):
        if not all(tile in self.player_tiles for tile in word):
            raise ValueError("El jugador no tiene las fichas necesarias.")
        
        for tile in word:
            self.player_tiles.remove(tile = Tile)

    def take_tiles(self, tiles):
        self.player_tiles.extend(tiles)
    
    def exchange_tiles(self, bag, letters):
        replaced_tiles = []
        for letter in letters:
            for tile in self.player_tiles:
                if tile == letter:
                    self.player_tiles.remove(tile)
                    replaced_tiles.append(tile)
                    break

        new_tiles = bag.take(len(replaced_tiles))
        self.player_tiles.extend(new_tiles)
        bag.put(replaced_tiles)
    
    def give_Tiles(self, letters):
        rackBackUp = self.rack.copy()
        tiles = []
        for i in range(len(letters)):
            letterIndex = -1
            for j in range(7 - i):
                if self.rack[j].letter == letters[i].upper(): 
                    letterIndex = j
                    break
            
            if letterIndex == -1:
                self.rack = rackBackUp
                raise MissingTileInRackException(letters[i] + " letter missing in rack.")
            else:
                tiles.append(self.rack.pop(letterIndex))
        return tiles   

    
