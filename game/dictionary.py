from pyrae import dle 

class DictionaryConnectionError(Exception):
    ...

dle.set_log_level(log_level='CRITICAL') 

class valid_word: 
    @staticmethod
    def is_in_dictionary(word):
        if word is not None:
            search = dle.search_by_word(word=str(word))
            if search is not None:
                return search.meta_description != 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
            else:
                raise DictionaryConnectionError("Error de conexión al buscar la palabra en el diccionario.")
        else:
            raise ValueError("La palabra no puede ser None.")        
        
