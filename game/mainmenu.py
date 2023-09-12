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
        except ValueError:
            print("please, define a valid value.")

def validate_number_of_players():
    while True:
        players = get_inputs()
        if is_valid_number_of_players(players):
            return players
        else:
            print("please, define a valid value (2-4).")

def main():
    print("WELLCOME TO SCRABBLE, by Juan Martin Valverde")

    players = validate_number_of_players()
    ScrabbleGame = ScrabbleGame(players)
    ScrabbleGame.begin_Match()

if __name__ == '__main__':
    main()
