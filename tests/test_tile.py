import unittest
from game.tiles import Tile

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
        
    def test_repr(self):
        tile = Tile('B', 1)
        expected = "B:1"
        actual = repr(tile)
        print(f"Expected: {expected}, Actual: {actual}")
        assert actual == expected

    def test_repr_ch(self):
        tile = Tile('Ch', 8)
        expected = "Ch:8"
        actual = repr(tile)
        print(f"Expected: {expected}, Actual: {actual}")
        assert actual == expected
        
