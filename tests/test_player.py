import unittest
from game.player import Player
from game.tiles import Tile
from game.bagtiles import BagTiles 

class TestPlayer(unittest.TestCase):    
    
    def test_init(self):
        player_id = 1
        player = Player(player_id)
        self.assertEqual(len( player.get_rack()), 0)
    
    def __repr__(self):
        return "TestPlayer"
    
    def test_get_player_id(self):
        player = Player(1)
        self.assertEqual(player.get_player_id(),1)
    
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
            player = Player(2)
            player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]

            tiles = [Tile('D', 2), Tile('E', 1)]
            player.take_tiles(tiles)

            expected_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]
            self.assertEqual([str(tile) for tile in player.player_rack], [str(tile) for tile in expected_rack])

    def test_give_tiles(self):
        player = Player(2)
        player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]

        letters = ["B", "D", "E"]
        tiles = player.give_tiles(letters)

        expected_tiles = [Tile('B', 3), Tile('D', 2), Tile('E', 1)]
        self.assertEqual([str(tile) for tile in tiles], [str(tile) for tile in expected_tiles])
        self.assertEqual([str(tile) for tile in player.player_rack], [str(tile) for tile in ['A (1)', 'C (3)']])
     
    def test_give_tiles_with_short_rack(self):
        player = Player(2)
        player.player_rack = [Tile("A", 1), Tile("B", 3), Tile("C", 3)]
        letters = ["A", "B", "C", "D", "E", "F", "G"]
        tiles = player.give_tiles(letters)
        self.assertEqual([str(tile) for tile in tiles], ['A (1)', 'B (3)', 'C (3)'])
        self.assertEqual([str(tile) for tile in player.player_rack], [])     
        
    def test_exchange_tiles(self):
        player = Player(2)
        player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]
        bag = BagTiles()
        bag.tiles = [Tile('F', 4), Tile('G', 2), Tile('H', 4), Tile('I', 1), Tile('J', 8)]

        letters = ['B', 'D', 'E']
        player.exchange_tiles(bag, letters)

        expected_rack = ['A (1)', 'C (3)', 'J (8)', 'I (1)', 'H (4)'] 
        self.assertEqual([str(tile) for tile in player.player_rack], [str(tile) for tile in expected_rack])
        self.assertEqual([str(tile) for tile in bag.tiles], ['F (4)', 'G (2)'])
    
    
    

# Rise value error

    def test_play_word_missing_tile(self):
        player = Player(2)
        player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]

        with self.assertRaises(ValueError):
            player.play_word([Tile('D', 2)])
            
    def test_exchange_tiles_with_missing_letter(self):
        player = Player(2)
        player.player_rack = [Tile("A", 1), Tile("B", 3)]
        letters = ["D"]
        with self.assertRaises(ValueError):
            player.exchange_tiles(BagTiles(), letters)
        self.assertEqual([str(tile) for tile in player.player_rack], ["A (1)", "B (3)"])   

    def test_give_tiles_with_missing_letter(self):
        player = Player(2)
        player.player_rack = [Tile("A", 1), Tile("B", 3), Tile("C", 3)]
        letters = ["D"]
        with self.assertRaises(ValueError):
            player.give_tiles(letters)
        self.assertEqual([str(tile) for tile in player.player_rack], ["A (1)", "B (3)", "C (3)"])
    
    def test_init_invalid_player_id(self):
        with self.assertRaises(ValueError):
            player = Player(player_id=None)
        with self.assertRaises(ValueError):
            player = Player(player_id='5')
        with self.assertRaises(ValueError):
            player = Player(player_id='6')
        with self.assertRaises(ValueError):
            player = Player(player_id='7')
        with self.assertRaises(ValueError):
            player = Player(player_id='8')
        with self.assertRaises(ValueError):
            player = Player(player_id='0')
        with self.assertRaises(ValueError):
            player = Player(player_id='1')