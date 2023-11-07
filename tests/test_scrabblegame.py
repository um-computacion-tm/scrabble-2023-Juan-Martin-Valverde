import unittest
from game.scrabblegame import ScrabbleGame
from game.tiles import Tile
from game.board import Board
from unittest.mock import patch
from game.bagtiles import BagTiles
from game.player import Player
from game.dictionary import valid_word

class TestScrabblePlayers(unittest.TestCase):

    def test_init_scrabble(self):
        scrabble_game = ScrabbleGame(total_players= 4)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players),4)
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]  
    
    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_round(self):
        # Arrange
        total_players = 3
        scrabble_game = ScrabbleGame(total_players=2)

        # Act
        current_player, round_number = scrabble_game.next_turn()

        # Assert
        expected_round_number = 2  # Se espera que la ronda se incremente a 2 después de la primera llamada a next_turn
        self.assertEqual(round_number, expected_round_number, "La ronda no se incrementa correctamente.")

        # Act nuevamente para verificar si la ronda sigue aumentando
        current_player, round_number = scrabble_game.next_turn()

        # Assert
        expected_round_number = 3  # Se espera que la ronda se incremente a 3 después de la segunda llamada a next_turn
        self.assertEqual(round_number, expected_round_number, "La ronda no se incrementa correctamente en el segundo turno.")

  