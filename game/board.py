

from game.cells import Cell
from game.bagtiles import BagTiles
from game.tiles import Tile
from game.dictionary import Dictionary



class Board:
    #defines the size of the table, the kind of multiplier and were they would be
    def __init__(self):
        emptyCell = Tile('',1)
        self.grid = [
            [ Cell(1, None) for _ in range(15) ]
            for _ in range(15)
        ]
        for i in range(4):
            for i in range(7):
                for j in range(7):
                    if i == 0:
                        self.grid[i][i] ==  Cell(emptyCell, 3, 'word')
                    elif i == 5:
                        self.grid[i][i] = Cell(emptyCell, 3, 'letter')  
                    elif i == 6:
                        self.grid[i][i] = Cell(emptyCell, 2, 'letter')   
                    else:
                        self.grid[i][i] = Cell(emptyCell, 2, 'word')
            self.grid[7][0] = Cell(emptyCell, 3, 'word')     
            self.grid[5][1] = Cell(emptyCell, 3, 'letter')   
            self.grid[1][5] = Cell(emptyCell, 3, 'letter')
            self.grid[0][3] = Cell(emptyCell, 2, 'letter')   
            self.grid[3][0] = Cell(emptyCell, 2, 'letter')
            self.grid[6][2] = Cell(emptyCell, 2, 'letter')
            self.grid[2][6] = Cell(emptyCell, 2, 'letter')
            self.grid[7][3] = Cell(emptyCell, 2, 'letter')
    
    #Let tha player put the word that he wants
    def put_word(self, word, location, orientation):
        N = location[0] - 1
        M = location[1] - 1
        for i in word: 
            self.grid[N][M].letter= i
            if orientation == 'H':
                M += 1
            elif orientation == 'V': 
                N += 1
    
    #As it name says it calculate the value of the word whit or whitout multiplier           
    def calculate_word_value(self, word, cell):
        word_value = 0
        word_multiplier = 1
        word_to_calculate = []
        for i in word:
            word_value += i.calculate_value()
            if i.multiplier_type == 'word':
                word_multiplier = i.multiplier   
                i.multiplier_type = None         
        word_value *= word_multiplier            
        return(word_value)
    
class MissingTileInRackException(Exception):
    pass

    
if __name__ == '__main__':
    pass