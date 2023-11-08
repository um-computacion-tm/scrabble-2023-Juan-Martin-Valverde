from game.bagtiles import BagTiles
from game.tiles import Tile
import random

class Player:
    def __init__(self, id = None, bag_tiles = None):
        self.id = id
        self.playertiles = []
        self.score = 0
        self.bag_tiles = bag_tiles if bag_tiles is not None else BagTiles()

    def reset (self):
        self.playertiles = []
    
    def get_tiles(self, bag:BagTiles, count):
        self.playertiles.extend(bag.take(count))

    def play_word(self, word):
        if self.has_letter(word):
            played_tiles = []
            for letter in word:
                for tile in self.playertiles:
                    if tile.letter == letter:
                        played_tiles.append(tile)
                        self.playertiles.remove(tile)
                        break
            return played_tiles
        else:
            return False

    def has_letter(self, word): 
        tiles = [tile.letter for tile in self.playertiles]
        for letter in word:
            if letter in tiles:
                tiles.remove(letter)
            else:
                return False
        return True

    def show_tiles(self):
        atril = " | ".join(f"{tile.letter}:{tile.value}" for tile in self.playertiles)
        indices = f"indx:" + " " * 3 + "  ".join(str(i + 1).center(4) for i in range(len(self.playertiles)))
        return (f"Player ID: {self.id}\nPuntaje: {self.score}\nAtril: {atril} |\n{indices}").rstrip()

    def __repr__(self):
        return self.show_tiles()
    
    def player_has_comodin(self):
        for tile in self.playertiles:
            if tile.letter == '?':
                return True
        return False
    
    def change_comodin_to_tiles(self, letter):
        comodin_tile = next((tile for tile in self.playertiles if tile.letter == '?'), None)
        if comodin_tile:
            comodin_tile.letter = letter.upper()
            comodin_tile.value = 0
        else:
            raise Exception("No tienes un comodin en tu atril.")

    def calculate_new_score (self, score):
        self.score += score

#23/32