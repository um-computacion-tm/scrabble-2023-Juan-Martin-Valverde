import unittest

from game.Models import (
    
    Tile,
    
    BagTiles,
    
    Board,
    
    Cell,
    
    Player,
    
    ScrabbleGame,
        
    )


from unittest.mock import patch


class TestTiles(unittest.TestCase):

    def test_tile_creation():
        tile_a = Tile('A', 1)
        tile_b = Tile('B', 3)
        tile_blank = Tile(' ', 0)

        assert tile_a.letter == 'A'
        assert tile_a.value == 1

        assert tile_b.letter == 'B'
        assert tile_b.value == 3

        assert tile_blank.letter == ' '
        assert tile_blank.value == 0



class TestBagTiles(unittest.TestCase):

   def test_bag_tiles():
        bag = BagTiles()

        taken_tiles = bag.take(7)

        assert len(taken_tiles) == 7

        bag.put(taken_tiles)

        more_taken_tiles = bag.take(5)

        assert len(more_taken_tiles) == 5

    
    
class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

    def test_put(self):

        bag = BagTiles()

        put_tiles = [Tile('Z', 1), Tile('Y', 1)]

        bag.put(put_tiles)

        self.assertEqual(

            len(bag.tiles),

            101,

        )


class TestCell(unittest.TestCase):

    def test_cell():
        tile_a = Tile('A', 1)
        tile_b = Tile('B', 3)
        
        cell_letter = Cell(2, 'letter')
        cell_word = Cell(3, 'word')
        
        cell_letter.add_letter(tile_a)
        cell_word.add_letter(tile_b)
        
        assert cell_letter.calculate_multiplier() == 2
        assert cell_word.calculate_multiplier() == 9
        
        
        empty_cell = Cell(2, 'letter')
        assert empty_cell.calculate_multiplier() == 0
        
        

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
        
        
class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)        


class TestCalculateWordValue(unittest.TestCase):
    def TestCalculateWordValue(self):
        word = [
        Cell(letter=Tile('C', 1)),
        Cell(letter=Tile('A', 1)),
        Cell(letter=Tile('S', 2)), 
        Cell(letter=Tile('A', 1)),
        ]

if __name__ == '__main__':

    unittest.main()
