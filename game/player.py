from game.tile import Tile
class MissingTileInRackException(Exception):
    pass

class Player:

    def play_word(self, word):
        if not all(tile in self.tiles for tile in word):
            raise ValueError("El jugador no tiene las fichas necesarias.")
        if all(tile in self.tiles for tile in word):
            for tile in word:
                self.tiles.remove(tile)
            return True
    def __init__(self, id=int):
        self.tiles = []
        self.id = id
        
    def take_Tiles(self, tiles):
        for tile in tiles:
            self.rack.append(tile)
            
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
    
if __name__ == '__main__':
    pass