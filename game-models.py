class Tile:
    def __init__(self, letter, value): 
        self.letter = letter 
        self.value = value

class BagTiles:
    def __init__(self):
        Self.Tiles = [
            
            Tile('A', 1),

            Tile('A', 1),

            Tile('A', 1),

            Tile('A', 1),

            Tile('A', 1),
        
            Tile('b', 2),
            
        ]
        
        random.shuffle(self.tiles)



    def take(self, count):

        tiles = []

        for _ in range(count):

            tiles.append(self.tiles.pop())

        return tiles



    def put(self, tiles):

        self.tiles.extend(tiles)