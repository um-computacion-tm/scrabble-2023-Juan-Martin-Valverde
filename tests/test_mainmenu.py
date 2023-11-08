import unittest
from unittest.mock import patch, MagicMock, Mock
from game.mainmenu import Main_Menu
from game.scrabblegame import ScrabbleGame

class TestMainMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Main_Menu()
        self.menu.scrabble = Mock()
        self.menu.scrabble.board = "Test Board"
        self.menu.scrabble.get_current_player.return_value = "Player 1"
    
    @patch('builtins.input', return_value='2')
    def test_get_player_count(self, input):
        self.assertEqual(self.menu.get_player_count(), 2)

    @patch('builtins.input', side_effect=['4', '2'])
    def test_get_player_count_invalid_then_valid(self, input):
        self.assertEqual(self.menu.get_player_count(), 4)

    @patch('builtins.print')
    def test_welcome_message(self, mock_print):
        self.menu.welcome_message()
        calls = [ 
            unittest.mock.call("______________________________________________________________________________________________"),
            unittest.mock.call("------------------------------------Bienvenido a Scrabble-------------------------------------")
        ]
        mock_print.assert_has_calls(calls)

    @patch('builtins.input', side_effect=['invalid', '2'])
    @patch('builtins.print')
    def test_get_player_count_invalid_input(self, mock_print, mock_input):
        self.assertEqual(self.menu.get_player_count(), 2)
        mock_print.assert_called_once_with("Valor invalido. Por favor ingresa un NUMERO VALIDO")    

    @patch('builtins.print')
    def test_show_game_options(self, mock_print):
        self.menu.show_game_options()
        calls = [ 
            unittest.mock.call("--------------------------------------Tabla de Scrabble-----------------------------------"),
            unittest.mock.call("Test Board"),
            unittest.mock.call("|------------------------------------------Opciones------------------------------------------|"),
            unittest.mock.call("|Preciona 1 para poner una palabra                                                           |"),
            unittest.mock.call("|Preciona 2 para cambiar tus letras                                                          |"),
            unittest.mock.call("|Preciona 3 para cambiar todas tus letras                                                    |"),
            unittest.mock.call("|Preciona 4 para cambiar el comodin                                                          |"),
            unittest.mock.call("|Preciona 5 para saltear el turno                                                            |"),
            unittest.mock.call("|Preciona 6 para terminar el juego                                                           |"),
            unittest.mock.call("|____________________________________________________________________________________________|"),
            unittest.mock.call("Player 1")
        ]
        mock_print.assert_has_calls(calls)
        
    @patch('builtins.input', return_value='valid')
    def test_get_word_input_valid(self, mock_input):
        self.assertEqual(self.menu.get_word_input(), 'VALID')

    @patch('builtins.input', side_effect=['123', 'valid'])
    @patch('builtins.print')
    def test_get_word_input_invalid_then_valid(self, mock_print, mock_input):
        self.assertEqual(self.menu.get_word_input(), 'VALID')
        mock_print.assert_called_once_with("Palabra invalida.Por favor ingresa solo caracteres alfabeticos.")
        
    @patch('builtins.input', side_effect=['1', '2'])
    def test_get_coordinates_valid(self, mock_input):
        self.assertEqual(self.menu.get_coordinates(), (1, 2))

    @patch('builtins.input', side_effect=['invalid', '1', '2'])
    @patch('builtins.print')
    def test_get_coordinates_invalid_then_valid(self, mock_print, mock_input):
        self.assertEqual(self.menu.get_coordinates(), (1, 2))
        mock_print.assert_called_once_with("Valor invalido. Por favor ingrese una coordenada valida.")

    @patch('builtins.input', return_value='h')
    def test_get_orientation_valid(self, mock_input):
        self.assertEqual(self.menu.get_orientation(), 'H')

    @patch('builtins.input', side_effect=['invalid', 'h'])
    @patch('builtins.print')
    def test_get_orientation_invalid_then_valid(self, mock_print, mock_input):
        self.assertEqual(self.menu.get_orientation(), 'H')
        mock_print.assert_called_once_with("Valor invalido. por favor ingresa 'H' para horizontal o 'V' para vertical.")

class TestMainMenu2(unittest.TestCase):
    
    @patch('builtins.input', return_value='1,1')
    @patch.object(Main_Menu, 'get_word_input', return_value='word')
    @patch.object(Main_Menu, 'get_coordinates', return_value=(1, 1))
    @patch.object(Main_Menu, 'get_orientation', return_value='H')
    @patch.object(ScrabbleGame, 'play_first_round')
    @patch.object(ScrabbleGame, 'play')
    def test_handle_user_input_option_1(self, mock_play, mock_play_first_round, mock_get_orientation, mock_get_coordinates, mock_get_word_input, mock_input):
        menu = Main_Menu()
        menu.scrabble = MagicMock()
        menu.scrabble.round = 1
        menu.handle_user_input(1)
        mock_get_word_input.assert_called_once()
        mock_get_coordinates.assert_called_once()
        mock_get_orientation.assert_called_once()
        mock_play.assert_not_called()
    
    @patch('builtins.input', return_value='1,2,3')
    def test_exchange_tiles(self, input):
        
        menu = Main_Menu()
        
        menu.scrabble = unittest.mock.Mock()
        menu.scrabble.exchange_tiles.return_value = ['A', 'B', 'C']

        menu.handle_user_input(2)

        menu.scrabble.exchange_tiles.assert_called_once_with([1, 2, 3])
        
        self.assertEqual(menu.exchanged_tiles, ['A', 'B', 'C'])
        
    def test_exchange_all_tiles(self):
        
        menu = Main_Menu()

        menu.scrabble = unittest.mock.Mock()
        menu.scrabble.exchange_all_tiles.return_value = ['A', 'B', 'C']

        exchanged_tiles = menu.scrabble.exchange_all_tiles()

        menu.scrabble.exchange_all_tiles.assert_called_once()

        self.assertEqual(exchanged_tiles, ['A', 'B', 'C'])
        
