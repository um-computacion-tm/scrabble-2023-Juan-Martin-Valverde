from game.tiles import Tile

class Cell:
    def __init__(self, multiplier='', multiplier_type='', active=True, multiplier_used=False):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None
        self.active = active
        self.multiplier_used = multiplier_used
        
    def add_letter(self, letter, new_multiplier_used=False):
        self.letter = letter
        self.active = False
        self.calculate_value(new_multiplier_used)
        
    def calculate_value(self, new_multiplier_used=False):
        if self.letter is None:
            return 0
        value = self.letter.value
        if self.active:
            if self.multiplier_type == 'letter':
                if not self.multiplier_used and not new_multiplier_used:
                    value *= self.multiplier
                    self.multiplier_used = True
            elif self.multiplier_type == 'word':
                if not self.multiplier_used and not new_multiplier_used:
                    value *= self.multiplier
                    self.multiplier_used = True
        return value