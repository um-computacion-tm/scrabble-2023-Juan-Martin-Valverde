from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles
from game.cells import Cell 
from game.tiles import Tile


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.players = [Player(player_id) for player_id in range(1, players_count + 1)]
        self.bag_tiles = BagTiles()
        self.current_player = None
    
    def calculate_final_score(self, player):
        score = 0
        for row in self.board.grid:
            for cell in row:
                if cell.letter is not None:
                    score += cell.calculate_value()

        for tile in player.player_rack:
            score += tile.value

        return score
    
    def begin_Match(self):
        for player in self.players:
            tilesToDraw = 7 - len(player.player_rack)
            newTiles = self.bag_tiles.take(tilesToDraw)     
            player.player_rack.extend(newTiles)
            
        self.current_player = self.players[0]
       
    def next_turn(self):
        if self.current_player is None:
            self.current_player = 0
        elif (self.players.index(self.current_player) != len(self.players) - 1):
            index = self.players.index(self.current_player) + 1
            self.current_player = index
        else: 
            self.current_player = 0
            
        if not self.bag_tiles.tiles:
            self.end_game()   
    """        
    def end_game(self):
        print("The game is over.")
        for player in self.players:
            print(f"The final score of {player.player_id} is {self.calculate_final_score(player)}")
        self.current_player = None
        """
        
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
    
