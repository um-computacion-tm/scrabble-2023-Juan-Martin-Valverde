import unittest
from game.bagtiles import BagTiles
from unittest.mock import patch

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(bag.calculate_tiles, 100)
        self.assertEqual(patch_shuffle.call_count,1)
        self.assertEqual(patch_shuffle.call_args[0][0],bag.total_tiles,)

    def test_calculate_total(self):
        bag = BagTiles()
        self.assertEqual(bag.total_tiles ,100)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(bag.total_tiles, 98)
        self.assertEqual((tiles),2)

    def test_put(self):
        bag = BagTiles()
        put_tiles = [('Z', 10),('U', 1)]
        bag.put(put_tiles)
        self.assertEqual(bag.total_tiles,100) #tiene que ser 102

