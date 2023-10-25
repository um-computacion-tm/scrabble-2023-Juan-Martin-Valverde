import unittest
from game.player import Player
from game.tiles import Tile
from game.bagtiles import BagTiles 
class TestPlayer(unittest.TestCase):
    
    def test_init(self):
        player_id = 1
        player = Player(player_id)
        self.assertEqual(len( player.get_rack()), 0)

    def test_get_player_id(self):
        player = Player(1)
        self.assertEqual(player.get_player_id(), 1)
    
    def test_play_word_valid(self):
        player = 1
        player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]

        word_to_play = [player.player_rack[0], player.player_rack[1]]
        result = player.play_word(word_to_play)

        self.assertTrue(result)
        self.assertEqual(len(player.player_rack), 1)
   
    def test_play_word_valid(self):
        player_id = 1
        player = Player(player_id)
        player.player_rack = ([Tile('A', 1), Tile('B', 3), Tile('C', 3)])

        word_to_play = [player.get_rack()[0], player.get_rack()[1]]
        result = player.play_word(word_to_play)

        self.assertTrue(result)
        self.assertEqual(len(player.get_rack()), 1)
    
    def test_take_tiles(self):
            player = Player(1)
            player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]

            tiles = [Tile('D', 2), Tile('E', 1)]
            player.take_tiles(tiles)

            expected_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]
            self.assertEqual([str(tile) for tile in player.player_rack], [str(tile) for tile in expected_rack])
    
    """
    def test_give_tiles(self):
        player = Player(1)
        player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]

        letters = ['B', 'D', 'E']
        tiles = player.give_tiles(letters)

        expected_tiles = [Tile('B', 3), Tile('D', 2), Tile('E', 1)]
        self.assertEqual([str(tile) for tile in tiles], [str(tile) for tile in expected_tiles])
        self.assertEqual([str(tile) for tile in player.player_rack], ['A', 'C'])
    """
    """
    def test_exchange_tiles(self):
        player = Player(1)
        player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]
        bag = BagTiles()
        bag.tiles = [Tile('F', 4), Tile('G', 2), Tile('H', 4), Tile('I', 1), Tile('J', 8)]

        letters = ['B', 'D', 'E']
        player.exchange_tiles(bag, letters)

        expected_rack = [Tile('A', 1), Tile('C', 3), Tile('F', 4), Tile('G', 2), Tile('H', 4), Tile('I', 1)]
        self.assertEqual([str(tile) for tile in player.player_rack], [str(tile) for tile in expected_rack])
        self.assertEqual([str(tile) for tile in bag.tiles], ['B', 'D', 'E', 'J'])
    """
    """
    def test_take_tiles(self):
        player = Player(1)
        player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]

        tiles = [Tile('D', 2), Tile('E', 1)]
        player.take_tiles(tiles)

        expected_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]
        self.assertEqual([str(tile) for tile in player.player_rack], [str(tile) for tile in expected_rack])    
"""

# Rise value error


    def test_init_invalid_player_id(self):
        with self.assertRaises(ValueError):
            player = Player(0)
        with self.assertRaises(ValueError):
            player = Player(5)

    def test_play_word_missing_tile(self):
        player = Player(1)
        player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]

        with self.assertRaises(ValueError):
            player.play_word([Tile('D', 2)])
    