from game.scrabblegame import ScrabbleGame
from game.player import Player 
from game.bagtiles import BagTiles

def is_valid_number_of_players(num):
    return 1 <= num <= 4

def get_inputs():
    while True:
        try:
            players = int(input("How many player will be? (2-4): "))
            if 1 <= players <= 4:
                return players
            else:
                print("Please enter a valid number between 2 and 4.")
        except ValueError:
            print("Please enter a valid number between 2 and 4.")

def validate_number_of_players():
    while True:
        players = get_inputs()
        if is_valid_number_of_players(players):
            return players
        else:
            print("please, define a valid value (2-4).")

def main():
    print("¡Bienvenido a Scrabble!")
    num_players = validate_number_of_players()

    players = validate_number_of_players()
    scrabble_game = ScrabbleGame(players)
    scrabble_game.begin_Match

