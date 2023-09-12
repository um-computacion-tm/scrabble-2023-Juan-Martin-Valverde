

from game.cells import Cell
from game.bagtiles import BagTiles
from game.tiles import Tile
from game.dictionary import Dictionary


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, 'letter') for _ in range(15) ]
            for _ in range(15)
        ]

  
    def check_word(self, word, file_path):
        with open(file_path, "r") as file:
            words = file.read().splitlines()
            if word in words:
                return True
            else:
                return False
            


    def calculate_word_value(self,word):
        aux = 0
        sum = 0
        list = []
        for aux in range(len(word)):
            
            if word[aux].active == False:
                word[aux].multiplier = 1
            
            if word[aux].multiplier_type == 'letter':
                sum += (word[aux].letter.value * word[aux].multiplier)
            else:
                sum += word[aux].letter.value
                list.append(aux)
        for _ in list:
            sum = sum * word[_].multiplier 
        return sum
    
if __name__ == '__main__':
    pass