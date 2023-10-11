import unittest
from game.board import Board
from game.cells import Cell
from game.tiles import Tile

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


    def test_board_cell_03(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[0][3].multiplier,3 )
        self.assertEqual(cell[0][3].multiplier_type,'word' )
    
    def test_board_cell_73(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[7][3].multiplier,2 )
        self.assertEqual(cell[7][3].multiplier_type,'word' )

    def test_put_word_horizontal(self):
        board = Board()
        position = [5,5]
        orientation = 'H'
        word = 'CASA'
        board.put_word(word, position, orientation)
        self.assertEqual(board.grid[4][4].letter, word[0])
        self.assertEqual(board.grid[4][5].letter, word[1])
        self.assertEqual(board.grid[4][6].letter, word[2])
        self.assertEqual(board.grid[4][7].letter, word[3])

    def test_put_word_vertical(self):
        board = Board()
        position = [5,5]
        orientation = 'V'
        word = [
            Tile('C',1),
            Tile('A',1),
            Tile('S',1),
            Tile('A',1),
                ]
        board.put_word(word, position, orientation)
        self.assertEqual(board.grid[4][4].letter.letter, word[0].letter)
        self.assertEqual(board.grid[5][4].letter.letter, word[1].letter)
        self.assertEqual(board.grid[6][4].letter.letter, word[2].letter)
        self.assertEqual(board.grid[7][4].letter.letter, word[3].letter)

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        tile1 = Tile('C', 1)
        cell1 = Cell(multiplier=1, multiplier_type='letter')
        cell1.add_letter(tile1)
        
        tile2 = Tile('A', 1)
        cell2 = Cell(multiplier=1, multiplier_type='letter')
        cell2.add_letter(tile2)
        
        tile3 = Tile('S', 2)
        cell3 = Cell(multiplier=1, multiplier_type='letter')
        cell3.add_letter(tile3)
        
        tile4 = Tile('A', 1)
        cell4 = Cell(multiplier=1, multiplier_type='letter')
        cell4.add_letter(tile4)
        board = Board()
        board.grid[7][7] = cell1
        board.grid[7][8] = cell2
        board.grid[7][9] = cell3
        board.grid[7][10] = cell4

        word = [cell1, cell2, cell3, cell4]
        start_row = 7
        start_col = 7
        direction = (0, 1)
        letter = cell1.letter 

        value = board.calculate_word_value(start_row, start_col, direction,letter, word)
        self.assertEqual(value, 14)
        
    def test_with_letter_multiplier(self):
        cell1 = Cell(multiplier=1,multiplier_type=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type=True)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        cell1 = Cell(multiplier=1,multiplier_type=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        cell1 = Cell(multiplier=3,multiplier_type=True)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        cell1 = Cell(multiplier=3,multiplier_type=True,active=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False,active=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type=True,active=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False,active=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 5)
    
    
