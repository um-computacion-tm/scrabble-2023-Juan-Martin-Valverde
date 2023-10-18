from typing import List, Tuple
from game.cells import Cell
from game.tiles import Tile
Empty_cell = Cell()

class Board:

    def __init__(self):
        self.grid = [[Cell() for _ in range(15)] for _ in range(15)]      
        self.grid[0][0] = Cell(3, 'word')
        self.grid[0][7] = Cell(3, 'word')
        self.grid[0][14] = Cell(3, 'word')
        self.grid[7][0] = Cell(3, 'word')
        self.grid[7][14] = Cell(3, 'word')
        self.grid[14][0] = Cell(3, 'word')
        self.grid[14][7] = Cell(3, 'word')
        self.grid[14][14] = Cell(3, 'word')
        self.grid[1][1] = Cell(2, 'letter')
        self.grid[2][2] = Cell(2, 'letter')
        self.grid[3][3] = Cell(2, 'letter')
        self.grid[4][4] = Cell(2, 'letter')
        self.grid[10][10] = Cell(2, 'letter')
        self.grid[11][11] = Cell(2, 'letter')
        self.grid[12][12] = Cell(2, 'letter')
        self.grid[13][13] = Cell(2, 'letter')
        self.grid[1][13] = Cell(2, 'letter')
        self.grid[2][12] = Cell(2, 'letter')
        self.grid[3][11] = Cell(2, 'letter')
        self.grid[4][10] = Cell(2, 'letter')
        self.grid[10][4] = Cell(2, 'letter')
        self.grid[11][3] = Cell(2, 'letter')
        self.grid[12][2] = Cell(2, 'letter')
        self.grid[13][1] = Cell(2, 'letter')
        self.grid[7][3] = Cell(2, 'letter')
        self.grid[5][1] = Cell(3, 'letter')
        self.grid[1][5] = Cell(3, 'letter')
        self.grid[0][3] = Cell(2, 'letter')
        self.grid[3][0] = Cell(2, 'letter')
        self.grid[6][2] = Cell(2, 'letter')
        self.grid[2][6] = Cell(2, 'letter')

    def put_word(self, word, position, orientation):
        N = position[0] - 1
        M = position[1] - 1
        for i in word: 
            self.grid[N][M].letter= i
            if orientation == 'H':
                M += 1
            elif orientation == 'V': 
                N += 1

    def calculate_word_value(self, word: List[Cell]) -> int:
        value = 0
        word_multiplier = 1
        for cell in word:
            if cell.letter is None:
                return 0
            cell_value = cell.calculate_value()
            if cell.multiplier_type == 'letter':
                cell_value *= cell.multiplier
            elif cell.multiplier_type == 'word':
                word_multiplier *= cell.multiplier
            value += cell_value
        return value * word_multiplier
    
    def is_valid(self, word: List[Cell]) -> bool:
        for cell in word:
            if cell.letter is None:
                return False
        return True
    
    def is_valid_position(self, word: List[Cell], position: List[int], orientation: str) -> bool:
        row, col = position
        if orientation == 'H':
            if col + len(word) > 15:
                return False
        else:
            if row + len(word) > 15:
                return False
        return True

   

   
   
    