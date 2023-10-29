import unittest
from game.tiles import Tile
from game.bagtiles import BagTiles
from unittest.mock import patch


class TestBagTiles(unittest.TestCase):
    
    def setUp(self):
        self.bag = BagTiles()

    
    
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles), 101)
        self.assertEqual(patch_shuffle.call_count, 1)
        self.assertEqual(patch_shuffle.call_args[0][0], bag.tiles)    
    
    def test_take(self):
        tiles = self.bag.take(7)
        self.assertEqual(len(tiles), 7)
        self.assertEqual(self.bag.total_tiles, 94)
        
    def test_put(self):
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        self.bag.put(tiles)
        self.assertEqual(self.bag.total_tiles, 101)
        
    def test_calculate_tiles(self):
        self.assertEqual(self.bag.calculate_tiles(), 101)
        
    def test_take_more_than_available(self):
        tiles = self.bag.take(102)
        self.assertEqual(len(tiles), 101)
        self.assertEqual(self.bag.total_tiles, 0)
    
    def test_take_all(self):
        tiles = self.bag.take(101)
        self.assertEqual(len(tiles), 101)
        self.assertEqual(self.bag.total_tiles, 0)
    
    def test_take_one(self):
        tiles = self.bag.take(1)
        self.assertEqual(len(tiles), 1)
        self.assertEqual(self.bag.total_tiles, 100)
    
    def test_take_zero(self):
        tiles = self.bag.take(0)
        self.assertEqual(len(tiles), 0)
        self.assertEqual(self.bag.total_tiles, 101)

    

    
        

