import unittest
from game.tiles import Tile

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('Z', 10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.value, 10)
    
 