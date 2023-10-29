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
        self.index = 0
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif (self.index != len(self.players) - 1):
            self.index += 1
            self.current_player = self.players[self.index]
        else: 
            self.index = 0
            self.current_player = self.players[self.index]
            
        if not self.bag_tiles.tiles:
            self.end_game()
            raise SystemExit("No more tiles in the bag.")
    
    def __repr__(self):
        return f"ScrabbleGame(players={self.players}, current_player={self.current_player}, board={self.board}, bag_tiles={self.bag_tiles})"
    
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
                       
    def end_game(self):
        print("The game is over.")
        for player in self.players:
            print(f"The final score of {player.player_id} is {self.calculate_final_score(player)}")
        self.current_player = None
        for player in self.players:
            player.player_rack = []
        self.bag_tiles.tiles = []

    
    
