from game.tiles import Tile

class Cell:
    def __init__(self, letter = None, multiplier = 1, multiplierType=None ):
        self.multiplier = multiplier
        self.multiplier_type = multiplierType
        self.letter = letter

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        
        if self.letter is None:
            return 0
        
        if self.multiplier_type == 'letter':
            value =self.letter.value * self.multiplier
            self.multiplier_type = None
            return value

        else:
            return self.letter.value
        