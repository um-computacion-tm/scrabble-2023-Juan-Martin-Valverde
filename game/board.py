from game.cells import Cell
from game.tiles import Tile
from game.dictionary import valid_word


class InvalidLocation(Exception):
    pass
class InvalidWord(Exception):
    pass
#word x3 multiplier position
Wx3 = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
#word x2 multiplier position
Wx2= ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
#letter x3 multiplier position
Lx3 = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
#letter x2 multiplier position
Lx2 = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

class Board:
    def __init__(self): 
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]
        self.get_multipliers()
        self.dictionary = valid_word()
    
    def valid_word_in_place(self, word, location, orientation):
        if not self.no_tiles_placed(word, location, orientation):
            if self.has_crossword(word, location, orientation):
                return False
        else:
            if self.has_neighbor_tile(word, location, orientation):
                if orientation == 'H' or orientation == 'h':
                    return self.find_and_validate_words_adjacent_horizontal(word, location) or self.find_and_validate_words_right_left(word, location)
                else:
                    return self.find_and_validate_words_adjacent_vertical(word, location) or self.find_and_validate_words_up_down(word, location)
            return False
        
    def valid_word_in_board(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        
        if (orientation == 'H' and x + word_length > 15) or (orientation == 'V' and y + word_length > 15):
            return False
        else:
            return True
    
    def no_tiles_placed(self, word, location, orientation):
        x, y = location
        for i in range(len(word)):
            check_x, check_y = (x + i, y) if orientation == 'H' else (x, y + i)
            if 0 <= check_x < 15 and 0 <= check_y < 15 and self.grid[check_x][check_y].tile:
                return False 
        return True   
        
    def has_neighbor_tile(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        word_and_neighbors = []
        for i in range(word_length):
            if orientation == 'H':
                word_and_neighbors.append((x, y + i))
                word_and_neighbors.append((x - 1, y + i))
                word_and_neighbors.append((x + 1, y + i))
            else:
                word_and_neighbors.append((x + i, y))
                word_and_neighbors.append((x + i, y - 1))
                word_and_neighbors.append((x + i, y + 1))

        for word_x, word_y in word_and_neighbors:
            if 0 <= word_x < 15 and 0 <= word_y < 15:

                if self.grid[word_x][word_y].tile:
                    return True
        return False
    

    def find_and_validate_words_up_and_down(self, word, location): 
        row, col = location
        formed_word = []
        
        if self.grid[row][col].tile:
            formed_word.append(self.grid[row][col].tile.letter)
        
        current_row, current_col = row - 1, col 
        while self.is_valid_position((current_row, current_col)) and self.grid[current_row][current_col].tile:
            formed_word.insert(0, self.grid[current_row][current_col].tile.letter)
            current_row -= 1

        current_row, current_col = row + len(word), col
        while self.is_valid_position((current_row, current_col)) and self.grid[current_row][current_col].tile:
            formed_word.append(self.grid[current_row][current_col].tile.letter)
            current_row += 1

        formed_word_str = ''.join(formed_word)
        formed_word_str_down = word + formed_word_str
        formed_word_str_up = formed_word_str + word
        if self.dictionary.is_in_dictionary(formed_word_str_up) or self.dictionary.is_in_dictionary(formed_word_str_down):
            return True, formed_word
        else:
            return False

    def find_and_validate_words_right_left(self, word, location): 
        row, col = location
        formed_word = []
        if self.grid[row][col].tile:
            formed_word.append(self.grid[row][col].tile.letter)

        current_row, current_col = row, col - 1
        while self.is_valid_position((current_row, current_col)) and self.grid[current_row][current_col].tile:
            formed_word.insert(0, self.grid[current_row][current_col].tile.letter)
            current_col -= 1

        current_row, current_col = row, col + len(word)
        while self.is_valid_position((current_row, current_col)) and self.grid[current_row][current_col].tile:
            formed_word.append(self.grid[current_row][current_col].tile.letter)
            current_col += 1

        formed_word_str = ''.join(formed_word)
        formed_word_str_left = formed_word_str + word
        formed_word_str_right = word + formed_word_str
        if self.dictionary.is_in_dictionary(formed_word_str_left) or self.dictionary.is_in_dictionary(formed_word_str_right):
            return True, formed_word
        else:
            return False

         
    def find_and_validate_words_adjacent_horizontal(self, word, location):
        row, col = location
        formed_words = []

        for i, letter in enumerate(word):
            formed_word = [letter]
            current_row, current_col = row, col

            while self.is_valid_position((current_row - 1, current_col)) and self.grid[current_row - 1][current_col].tile:
                current_row -= 1
                formed_word.insert(0, self.grid[current_row][current_col].tile.letter)
                
            current_row, current_col = row, col

            while self.is_valid_position((current_row + 1, current_col)) and self.grid[current_row + 1][current_col].tile:
                current_row += 1
                formed_word.append(self.grid[current_row][current_col].tile.letter)

            formed_word_str = ''.join(formed_word)
            if len(formed_word_str) > 1 and self.dictionary.is_in_dictionary(formed_word_str):
                formed_words.append(formed_word_str)
            elif len(formed_word_str) > 1 and not self.dictionary.is_in_dictionary(formed_word_str):
                return False

            col += 1

        return formed_words



    def get_direction(self, orientation):
        if orientation == 'H':
            return (1, 0)  
        elif orientation == 'V':
            return (0, 1) 
        else:
            raise ValueError("Invalid orientation")


    def is_valid_position(self, position):
        x, y = position
        return 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid)

    def has_crossword(self, word, location, orientation):
        x, y = location       
        for i, letter in enumerate(word):
            cross_x, cross_y = (x + i, y) if orientation == 'H' else (x, y + i)

            if 0 <= cross_x < 15 and 0 <= cross_y < 15 and self.grid[cross_x][cross_y].tile:
                existing_tile = self.grid[cross_x][cross_y].tile                
                if existing_tile.letter != letter:
                    return False
        return True
    
    
    @staticmethod
    def calculate_word_score(word:list[Cell]) -> int:
        value: int = 0
        multiplier_word = 1
        for cell in word:
            value = value + cell.calculate_letter_score()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
                cell.multiplier_type = None
                cell.active = False
        if multiplier_word:
            value = value * multiplier_word
        return value

    def is_empty(self):
        if self.grid[7][7].tile is None:
            return True
        else:
            return False   
        
    def put_word(self, word, location, orientation):
        if orientation.upper()== 'H':
            for i in range(len(word)):
                self.grid[location[0]][location[1]+i].add_tile(word[i])
        else:
            for i in range(len(word)):
                self.grid[location[0]+i][location[1]].add_tile(word[i])
    
    def put_first_word(self, word, location, orientation):
        x, y = 7,7

        if location != (x, y):
            raise InvalidLocation('La primera palabra tiene que estar en la posicion(7,7)')
        
        self.put_word(word, (x, y), orientation)
        

    def get_multipliers(self):
        for coordinate in Lx2:
            self.set_multipliers(coordinate, 2, 'letter')
        for coordinate in Lx3:
            self.set_multipliers(coordinate, 3, 'letter')
        for coordinate in Wx2:
            self.set_multipliers(coordinate, 2, 'word')
        for coordinate in Wx3:
            self.set_multipliers(coordinate, 3, 'word')
            
    def set_multipliers(self, coordinate, multiplier, multiplier_type):
        square = self.grid[coordinate[0]][coordinate[1]]
        square.multiplier = multiplier
        square.multiplier_type = multiplier_type


#I liked how vicente cara tapia made it so I copied it

    def __repr__(self): 
        spaces = " " * 4
        horizontal_line = spaces + "┌" + "─────┬" * 14 + "─────┐" + "\n"
        middle_horizontal_line = spaces + "├" + "─────┼" * 14 + "─────┤" + "\n"
        bottom_horizontal_line = spaces + "└" + "─────┴" * 14 + "─────┘"

        board = " " * 5 + " ".join([str(i).center(5, " ") for i in range(15)]) + "\n"
        board += horizontal_line

        for i in range(15):
            board += f"{str(i).rjust(3)} │"
            for j in range(15):
                cell = self.grid[i][j]
                if cell.tile is not None:
                    cell_repr = f"{cell.tile}".center(5, " ")
                elif cell.multiplier_type == 'letter':
                    cell_repr = f"Lx{cell.multiplier}".center(5, " ") 
                elif cell.multiplier_type == 'word':
                    cell_repr = f"Wx{cell.multiplier}".center(5, " ")
                else:
                    cell_repr = "     "
                board += cell_repr + "│"
            board += "\n"
            if i != 14:
                board += middle_horizontal_line
        board+= bottom_horizontal_line
        return board