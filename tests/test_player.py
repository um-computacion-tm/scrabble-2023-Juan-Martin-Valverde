import unittest
from game.player import Player
from game.bagtiles import BagTiles
from game.tiles import Tile

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player()
        self.assertEqual(len(player.playertiles),0)

    def test_reset(self):
        player = Player()
        player.playertiles = [Tile('A', 1),Tile('B', 1), Tile('Ch', 8)]
        player.reset()
        self.assertEqual(len(player.playertiles), 0)
   
    def test_get_tiles(self):
        player = Player()
        bag = BagTiles()
        initial_tiles_count = len(player.playertiles)
        player.get_tiles(bag, 7)
        self.assertEqual(len(player.playertiles), initial_tiles_count + 7)
    
    def test_validate_user_has_letters(self):
        player = Player()
        player.playertiles =[
            Tile(letter='A', value=1),
            Tile(letter='V', value=4),
            Tile(letter='I', value=1),
            Tile(letter='O', value=1),
            Tile(letter='N', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
        ]
        word = 'AVION'
        is_valid = player.has_letter(word)
        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        player = Player()
        player.playertiles = [
            Tile(letter='B', value=3),
            Tile(letter='I', value=1),
            Tile(letter='C', value=3),
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='N', value=1),
            Tile(letter='L', value=1),
        ]
        word = 'PICHON'
        is_valid = player.has_letter(word)
        self.assertEqual(is_valid, False)

    def test_validate_when_user_has_letter_ch_ll_rr(self):
        player = Player()
        player.playertiles = [
            Tile(letter='L', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='M', value=3),
            Tile(letter='A', value=1),
            Tile(letter='R', value=1),
            Tile(letter='O', value=1),
        ]
        word = 'LLAMAR'
        is_valid = player.has_letter(word)
        self.assertEqual(is_valid, True)

    def test_calculate_new_score(self):
        self.player = Player()
        initial_score = self.player.score
        new_score = 10
        self.player.calculate_new_score(new_score)
        self.assertEqual(self.player.score, initial_score + new_score)


#CHOOSE YOUR CHARACTER *EMPIEZA A SONAR LA MUSICA DE STREET FIRGHTER*

class TestPlayer1(unittest.TestCase):

    def test_play_valid_word(self):
        player = Player()
        player.playertiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='L', value=3),
        ]
        word = 'HOLA'
        result = player.play_word(word)
        self.assertTrue(result)
        self.assertEqual(len(player.playertiles), 3) 

    def test_play_invalid_word(self):
        player = Player()
        player.playertiles = [
            Tile(letter='C', value=4),
            Tile(letter='U', value=1),
            Tile(letter='L', value=1),
            Tile(letter='O', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        word = 'CAMPERA'
        result = player.play_word(word)
        self.assertFalse(result)
        self.assertEqual(len(player.playertiles), 7) 
        
    def test_show_tiles(self):
        player = Player()
        player.id = 1
        player.score = 10
        player.playertiles = [
            Tile(letter='M', value=3),
            Tile(letter='I', value=1),
            Tile(letter='N', value=1),
            Tile(letter='A', value=1),
            Tile(letter='S', value=1),
            Tile(letter='I', value=1),
            Tile(letter='N', value=1),
        ]
        expected_output = (
            "Player ID: 1\n"
            "Puntaje: 10\n"
            "Atril: M:3 | I:1 | N:1 | A:1 | S:1 | I:1 | N:1 |\n"
            "indx:    1     2     3     4     5     6     7"
        )
        self.assertEqual(player.show_tiles(), expected_output)
    
    def test_repr(self):
        player = Player()
        player.id = 1
        player.score = 10
        player.playertiles = [
            Tile(letter='M', value=3),
            Tile(letter='E', value=1),
            Tile(letter='S', value=1),
            Tile(letter='S', value=1),
            Tile(letter='I', value=1),
            Tile(letter='D', value=2),
            Tile(letter='I', value=1),
        ]
        expected_output = (
            "Player ID: 1\n"
            "Puntaje: 10\n"
            "Atril: M:3 | E:1 | S:1 | S:1 | I:1 | D:2 | I:1 |\n"
            "indx:    1     2     3     4     5     6     7"
        )
        self.assertEqual(repr(player), expected_output)

    def test_has_comodin_like_comodin(self):
        player = Player()
        player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='?', value=0),
            Tile(letter='B', value=3),
        ]
        has_comodin = player.player_has_comodin()
        self.assertTrue(has_comodin)

    def test_has_comodin_like_tile(self):
        player = Player()
        player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='B', value=3),
            Tile(letter='C', value=3),
        ]
        has_comodin = player.player_has_comodin()
        self.assertFalse(has_comodin)
    def test_convert_comodin_to_tile(self):
        player = Player()
        player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='?', value=0),
            Tile(letter='B', value=3),
            Tile(letter='C', value=3),
        ]

        player.change_comodin_to_tile('M')
        self.assertEqual(player.playertiles[1].letter, 'M')
        self.assertEqual(player.playertiles[1].value, 0)

        with self.assertRaises(Exception) as context:
            player.change_comodin_to_tile('E')
        self.assertEqual(
            str(context.exception), "No tienes un comodin en tu atril.")

        player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='B', value=3),
            Tile(letter='C', value=3),
        ]
        with self.assertRaises(Exception) as context:
            player.change_comodin_to_tile('E')
        self.assertEqual(
            str(context.exception), "No tienes un comodin en tu atril.")

