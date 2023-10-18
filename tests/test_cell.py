import unittest
from game.tiles import Tile
from game.cells import Cell

class TestCell(unittest.TestCase):
    def test_add_letter(self):
        tile = Tile('A', 1)
        cell = Cell()
        cell.add_letter(tile)
        self.assertEqual(cell.letter, tile)
        self.assertFalse(cell.active)

    def test_calculate_value_no_letter(self):
        cell = Cell()
        self.assertEqual(cell.calculate_value(), 0)

    def test_calculate_value_letter_no_multiplier(self):
        tile = Tile('A', 1)
        cell = Cell()
        cell.add_letter(tile)
        self.assertEqual(cell.calculate_value(), 1)

    def test_calculate_value_letter_multiplier_used(self):
        tile = Tile('A', 1)
        cell = Cell(multiplier=2, multiplier_type='letter', multiplier_used=True)
        cell.add_letter(tile)
        self.assertEqual(cell.calculate_value(), 1)
    """
    def test_calculate_value_letter_multiplier_not_used(self):
        tile = Tile('A', 1)
        cell = Cell(multiplier=2, multiplier_type='letter')
        cell.add_letter(tile)
        self.assertEqual(cell.calculate_value(), 2)
    """
    def test_calculate_value_word_multiplier_used(self):
        tile = Tile('A', 1)
        cell = Cell(multiplier=2, multiplier_type='word', multiplier_used=True)
        cell.add_letter(tile)
        self.assertEqual(cell.calculate_value(), 1)
    """
    def test_calculate_value_word_multiplier_not_used(self):
        tile = Tile('A', 1)
        cell = Cell(multiplier=2, multiplier_type='word', active=True, multiplier_used=False)
        cell.add_letter(tile)
        self.assertEqual(cell.calculate_value(), 2)
    """


