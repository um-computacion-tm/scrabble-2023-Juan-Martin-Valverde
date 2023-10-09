import random
from game.tiles import  Tile

class EmptyBagException(Exception):
    pass
#This one defines what would be the total of tiles on the game
class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile(' ', 0), Tile(' ', 0),                                                                 #2
            
            Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), 
            Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1),         #14A
            
            Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),    
            Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),         #14E
            
            Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1),         #7I
            
            Tile('L', 1), Tile('L', 1), Tile('L', 1), Tile('L', 1),                                     #4L
            
            Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1),                       #5N
            
            Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1),                                
            Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1),                       #9O
            
            Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1),                       #5R
            
            Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1),         #7S
            
            Tile('T', 1), Tile('T', 1), Tile('T', 1), Tile('T', 1),                                     #5T
            
            Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1),                       #6U
            
            Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2),                       #6D
            
            Tile('G', 2), Tile('G', 2),                                                                 #2G
            
            Tile('B', 3), Tile('B', 3),                                                                 #2B
            
            Tile('C', 3), Tile('C', 3), Tile('C', 3), Tile('C', 3),                                     #4C
            
            Tile('M', 3), Tile('M', 3),                                                                 #2M
            
            Tile('P', 3), Tile('P', 3),                                                                 #2P
            
            Tile('F', 4),                                                                               #1F
            
            Tile('H', 4), Tile('H', 4),                                                                 #2H
        
            Tile('V', 4),                                                                               #1V
            
            Tile('Y', 4),                                                                               #1Y
            
            Tile('Ch', 5),                                                                              #1CH
            
            Tile('Q', 5),                                                                               #1Q
            
            Tile('J', 8),                                                                               #1J
            
            Tile('Ll', 8),                                                                              #1LL
            
            Tile('Ñ', 8),                                                                               #1Ñ
            
            Tile('RR', 8),                                                                              #1RR
            
            Tile('X', 8),                                                                               #1X
            
            Tile('Z', 10)                                                                               #1Z
        ]
        self.total_tiles = self.calculate_tiles()
        random.shuffle(self.total_tiles)
#It calculate the amount of tiles that are on the bagtile
    def calculate_tiles(self):
        total_tiles = []
        for letter, value, total in self.tiles:
            total_tiles.extend([(letter, value)]* value)
            return total_tiles
#It let the player take one tile from the bag tile    
    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.total_tiles.pop())
        return tiles
#It let the palyer put one tile when he takes form the bagtile
    def put(self, tiles):
        self.total_tiles.extend(tiles)
        

