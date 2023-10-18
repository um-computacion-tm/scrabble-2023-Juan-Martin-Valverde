import random
from game.tiles import Tile

class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), 
            Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1),         #12A
            
            Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),    
            Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),         #12E
            
            Tile('I', 1), Tile('I', 1), Tile('I', 1), 
            Tile('I', 1), Tile('I', 1), Tile('I', 1),                                                   #6I
            
            Tile('L', 1), Tile('L', 1), Tile('L', 1), 
            Tile('L', 1), Tile('L', 1), Tile('L', 1),                                                   #6L
            
            Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1),                       #5N
            
            Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1),                                
            Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1),                       #9O
            
            Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1), 
            Tile('R', 1), Tile('R', 1), Tile('R', 1),                                                   #7R
            
            Tile('S', 1), Tile('S', 1), Tile('S', 1),                                                   #6S
            Tile('S', 1), Tile('S', 1), Tile('S', 1),
            
            Tile('T', 1), Tile('T', 1), Tile('T', 1), Tile('T', 1),                                     #4T
            
            Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1),                       #5U
            
            Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2),                       #5D
            
            Tile('G', 2), Tile('G', 2),                                                                 #2G
            
            Tile('B', 3), Tile('B', 3),                                                                 #2B
            
            Tile('C', 3), Tile('C', 3), Tile('C', 3), Tile('C', 3), Tile('C', 3),                       #5C
            
            Tile('M', 3), Tile('M', 3),                                                                 #2M
            
            Tile('P', 3), Tile('P', 3),                                                                 #2P
            
            Tile('F', 4),                                                                               #1F
            
            Tile('H', 4), Tile('H', 4), Tile('H', 4),                                                   #3H
        
            Tile('V', 4),                                                                               #1V
            
            Tile('Y', 4),                                                                               #1Y
            
            Tile('Q', 5),                                                                               #1Q
            
            Tile('J', 8),                                                                               #1J
            
            Tile('Ñ', 8),                                                                               #1Ñ
            
            Tile('X', 8),                                                                               #1X
            
            Tile('Z', 10)                                                                               #1Z
        ]
        self.total_tiles = self.calculate_tiles()
        random.shuffle(self.tiles)
        
    def calculate_tiles(self):
        return len(self.tiles)
        
    def take(self, count):
        tiles = []
        for _ in range(count):
            if self.total_tiles > 0:
                tiles.append(self.tiles.pop())
                self.total_tiles -= 1
        return tiles
        
    def put(self, tiles):
        self.tiles.extend(tiles)

