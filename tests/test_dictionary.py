import unittest
from unittest.mock import patch
from game.dictionary import(
    DictionaryConnectionError,
    valid_word
)

class TestDiccionary(unittest.TestCase):
    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='1. interj. U. como salutación familiar.'
        )
    )
    def test_valid(self, search_by_word_patched):
        self.assertTrue(valid_word.is_in_dictionary('hola'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        )
    )
    def test_invalid(self, search_by_word_patched):
        self.assertFalse(valid_word.is_in_dictionary('asd'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=None
    )
    def test_connection_error(self, search_by_word_patched):
        with self.assertRaises(DictionaryConnectionError):
            valid_word.is_in_dictionary('hola')
            
    def test_is_in_dictionary_with_none(self):
        vw = valid_word()
        with self.assertRaises(ValueError):
            vw.is_in_dictionary(None)
