import unittest
from game.scrabblegame import ScrabbleGame
from game.player import Player
from game.bagtiles import BagTiles

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players),3)
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_start_game(self):
        player = Player()
        game = ScrabbleGame(players_count = 3)
        game.start_game()

        for player in game.players:
            self.assertEqual(len(player.tiles), 7)

    def test_next_turn(self):
        game = ScrabbleGame(players_count=3)
        self.assertEqual(game.current_player, 0)
        game.next_turn()
        self.assertEqual(game.current_player, 1)
        game.next_turn()
        self.assertEqual(game.current_player, 2)
        game.next_turn()
        self.assertEqual(game.current_player, 0)
        game.next_turn()
        self.assertEqual(game.current_player, 1)

    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    
    def test_turns_2players(self):
        Game = ScrabbleGame(2)
        self.assertEqual(Game.turn, 0)
        Game.next_turn()
        self.assertEqual(Game.turn, 1)
        Game.next_turn()
        self.assertEqual(Game.turn, 0)
    
    def test_turns_4players(self):
        Game = ScrabbleGame(4)
        self.assertEqual(Game.turn, 0)
        Game.next_turn()
        self.assertEqual(Game.turn, 1)
        Game.next_turn()
        self.assertEqual(Game.turn, 2)
        Game.next_turn()
        self.assertEqual(Game.turn, 3)
        Game.next_turn()
        self.assertEqual(Game.turn, 0)

    def test_turn_0(self):
        Game = ScrabbleGame(2)
        self.assertEqual(Game.turn, 0)
        Game.next_turn()
        self.assertEqual(Game.turn, 1)
        Game.next_turn()
        self.assertEqual(Game.turn, 0)
        
if __name__ == '__main__':
    unittest.main()
    