import random

class EmptyBagException(Exception):
    pass

class OccupiedSquareException(Exception):
    pass

class MissingTileInRackException(Exception):
    pass

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('*', 0),
            Tile('*', 0),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
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
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('I', 1),
            Tile('L', 1),
            Tile('L', 1),
            Tile('L', 1),
            Tile('L', 1),
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
            Tile('O', 1),
            Tile('R', 1),
            Tile('R', 1),
            Tile('R', 1),
            Tile('R', 1),
            Tile('R', 1),
            Tile('S', 1),
            Tile('S', 1),
            Tile('S', 1),
            Tile('S', 1),
            Tile('S', 1),
            Tile('S', 1),
            Tile('T', 1),
            Tile('T', 1),
            Tile('T', 1),
            Tile('T', 1),
            Tile('U', 1),
            Tile('U', 1),
            Tile('U', 1),
            Tile('U', 1),
            Tile('U', 1),
            Tile('D', 2),
            Tile('D', 2),
            Tile('D', 2),
            Tile('D', 2),
            Tile('D', 2),
            Tile('G', 2),
            Tile('G', 2),
            Tile('B', 3),
            Tile('B', 3),
            Tile('C', 3),
            Tile('C', 3),
            Tile('C', 3),
            Tile('C', 3),
            Tile('M', 3),
            Tile('M', 3),
            Tile('P', 3),
            Tile('P', 3),
            Tile('F', 4),
            Tile('H', 4),
            Tile('H', 4),   
            Tile('V', 4),
            Tile('Y', 4),
            Tile('Ch', 5),
            Tile('Q', 5),
            Tile('J', 8),
            Tile('Ll', 8),
            Tile('Ñ', 8),
            Tile('RR', 8),
            Tile('X', 8),
            Tile('Z', 10)
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
        class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
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
        suma = 0
        list = []
        for aux in range(len(word)):
            
            if word[aux].active == False:
                word[aux].multiplier = 1
            
            if word[aux].multiplier_type == 'letter':
                suma += (word[aux].letter.value * word[aux].multiplier)
            else:
                suma += word[aux].letter.value
                list.append(aux)
        for _ in list:
            suma = suma * word[_].multiplier 
        return suma
    
class Player:
    def __init__(self, id=int):
        self.tiles = []
        self.id = id

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())

        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif (self.players.index(self.current_player) != len(self.players) - 1):

            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]
        else: 
            self.current_player = self.players[0]
            
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