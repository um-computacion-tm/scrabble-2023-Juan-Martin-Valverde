import random

class Tile:
    def __init__(self, letter, value): 
        self.letter = letter 
        self.value = value

class BagTiles:

    def __init__(self):

        self.tiles = [

            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('B', 3),
            Tile('B', 3),
            Tile('C', 3),
            Tile('C', 3),
            Tile('D', 2),
            Tile('D', 2),
            Tile('D', 2),
            Tile('D', 2),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('E', 1),
            Tile('F', 4),
            Tile('F', 4),
            Tile('G', 2),
            Tile('G', 2),
            Tile('G', 2),
            Tile('H', 4),
            Tile('H', 4),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('J', 8),
            Tile('K', 5),
            Tile('L', 1),
            Tile('L', 1),
            Tile('L', 1),
            Tile('L', 1),
            Tile('M', 3),
            Tile('M', 3),
            Tile('N', 1),
            Tile('N', 1),
            Tile('N', 1),
            Tile('N', 1),
            Tile('N', 1),
            Tile('N', 1),
            Tile('O', 1),
            Tile('O', 1),
            Tile('O', 1),
            Tile('O', 1),
            Tile('O', 1),
            Tile('O', 1),
            Tile('O', 1),
            Tile('O', 1),
            Tile('P', 3),
            Tile('P', 3),
            Tile('Q', 10),
            Tile('R', 1),
            Tile('R', 1),
            Tile('R', 1),
            Tile('R', 1),
            Tile('R', 1),
            Tile('R', 1),
            Tile('S', 1),
            Tile('S', 1),
            Tile('S', 1),
            Tile('S', 1),
            Tile('T', 1),
            Tile('T', 1),
            Tile('T', 1),
            Tile('T', 1),
            Tile('T', 1),
            Tile('T', 1),
            Tile('U', 1),
            Tile('U', 1),
            Tile('U', 1),
            Tile('U', 1),
            Tile('V', 4),
            Tile('V', 4),
            Tile('W', 4),
            Tile('W', 4),
            Tile('X', 8),
            Tile('Y', 4),
            Tile('Y', 4),
            Tile('Z', 10),
            Tile(' ', 0), 
        ]

        random.shuffle(self.tiles)



    def take(self, count):

        tiles = []

        for _ in range(count):

            tiles.append(self.tiles.pop())

        return tiles



    def put(self, tiles):

        self.tiles.extend(tiles)
        

class Cell:

    def __init__(self, multiplier, multiplier_type):

        self.multiplier = multiplier

        self.multiplier_type = multiplier_type

        self.letter = None

    def add_letter(self, letter:Tile):

        self.letter = letter

    def calculate_multipier(self):
        
        if self.letter is None: 
            return 0
        
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        
        else:
            return self.letter.value
         
class Board:
    def __init__(self):
        self.grid = [
            [Cell(self.multiplier(row, col)) for col in range(15)]
            for row in range(15)
        ]

    def multiplier(self, row, col):
        if (row, col) == (0, 0):
            return 'x3'
        elif (row, col) == (0, 7):
            return 'x2'
        else:
            return 'x1'
   

class Player:
    def __init__(self):
        self.tiles = []


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())
    
    
class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())

    def calculate_word_score(self, word, start_row, start_col, direction):
        score = 0
        word_multiplier = 1

        for i, letter in enumerate(word):
            row = start_row + (i * direction[0])
            col = start_col + (i * direction[1])
            cell = self.board.grid[row][col]

            letter_value = letter.value
            cell_multiplier = 1

            if cell.multiplier_type == 'letter':
                cell_multiplier = cell.multiplier
            elif cell.multiplier_type == 'word':
                word_multiplier *= cell.multiplier

            score += letter_value * cell_multiplier

        return score * word_multiplier