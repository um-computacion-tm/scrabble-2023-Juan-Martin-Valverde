from game.tiles import Tile
class MissingTileInRackException(Exception):
    pass

class Player:
    def __init__(self, player_id):
        self.tiles = []
        self.player_id = player_id

    def play_word(self, word):
        if not all(tile in self.tiles for tile in word):
            raise ValueError("El jugador no tiene las fichas necesarias.")
        
        for tile in word:
            self.tiles.remove(tile)

    def take_tiles(self, tiles):
        self.tiles.extend(tiles)
    
    def exchange_tiles(self, bag, letters):
        replaced_tiles = []
        for letter in letters:
            for tile in self.tiles:
                if tile.Tile == letter:
                    self.tiles.remove(tile)
                    replaced_tiles.append(tile)
                    break

        new_tiles = bag.take(len(replaced_tiles))
        self.tiles.extend(new_tiles)
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
    def get_rack(self):
        return self.tiles

    def get_player_id(self):
        return self.player_id
    
if __name__ == '__main__':
    pass