

from game.cells import Cell
from game.bagtiles import BagTiles
from game.tiles import Tile
from game.dictionary import Dictionary


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        
        ]
        self.grid[0][0] = Cell(1, '*')
        self.grid[0][7] = Cell(3, 'word')
        self.grid[0][14] = Cell(1, '*')

    
    def check_word(self, word, file_path):
        with open(file_path, "r") as file:
            words = file.read().splitlines()
            if word in words:
                return True
            else:
                return False
            


    def calculate_word_score(self, word, start_row, start_col, direction, letter:Tile):
        score = 0
        word_multiplier = 1

        for i, letter in enumerate(word):
            row = start_row + (i * direction[0])
            col = start_col + (i * direction[1])
            cell = self.grid[row][col]

            letter_value = letter.value
            cell_multiplier = 1

            if cell.special == 'DL':                    #DOBLE (LETRA)
                letter_value *= 2
            elif cell.special == 'TL':                  #TRIPLE (LETRA)
                letter_value *= 3
            elif cell.special == 'DW':                  #DOBLE (PALABRA)
                word_multiplier *= 2
            elif cell.special == 'TW':                  #TRIPLE (PALABRA)
                word_multiplier *= 3
            elif cell.special == '*':                   #COMODIN
                
                pass

            score += letter_value * cell_multiplier

        return score * word_multiplier

class MissingTileInRackException(Exception):
    pass

    
if __name__ == '__main__':
    pass