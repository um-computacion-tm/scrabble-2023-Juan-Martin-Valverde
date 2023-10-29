import unittest
from game.scrabblegame import ScrabbleGame
from game.player import Player
from game.bagtiles import BagTiles
from game.tiles import Tile
class TestScrabbleGame(unittest.TestCase):
    
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertIsNotNone(scrabble_game.bag_tiles)
        
    def test_start_game(self):
        game = ScrabbleGame(players_count=3)
        game.begin_Match()

        for player in game.players:
            self.assertEqual(len(player.player_rack), 7)
    
    def test_end_game(self):
        game = ScrabbleGame(players_count=3)
        game.begin_Match()
        game.end_game()
        self.assertEqual(game.current_player, None)
        self.assertEqual(game.players[0].player_rack, [])
        self.assertEqual(game.players[1].player_rack, [])
        self.assertEqual(game.players[2].player_rack, [])
        self.assertEqual(game.bag_tiles.tiles, [])
        
    def test_next_turn(self):
        game = ScrabbleGame(2)
        game.current_player = None
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 1)
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 2)
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 1)
        game.bag_tiles.tiles = []
        with self.assertRaises(SystemExit):
            game.next_turn()

    def test_turns_2players(self):
        game = ScrabbleGame(2)
        game.current_player = None
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 1)
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 2)
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 1)
    
    def test_turns_4players(self):
        game = ScrabbleGame(4)
        game.current_player = None
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 1)
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 2)
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 3)
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 4)
        game.next_turn()
        self.assertEqual(game.current_player.player_id, 1)

    def test_repr(self):
        game = ScrabbleGame(2)
        game.current_player = game.players[0]
        game.board.grid[0][0].letter = "A"
        game.bag_tiles.tiles = ["A", "B", "C"]
        expected_repr = f"ScrabbleGame(players={game.players}, current_player={game.current_player}, board={game.board}, bag_tiles={game.bag_tiles})"
        self.assertEqual(repr(game), expected_repr)
    
    def test_calculate_final_score(self):
        game = ScrabbleGame(players_count=2)
        player = Player(1)
        player.player_rack = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        game.board.grid[0][0].add_letter(Tile('A', 1))
        game.board.grid[0][1].add_letter(Tile('B', 3))
        game.board.grid[0][2].add_letter(Tile('C', 2))
        expected_score = 6 + 1 + 3 + 2
        self.assertEqual(game.calculate_final_score(player), expected_score)
       
        