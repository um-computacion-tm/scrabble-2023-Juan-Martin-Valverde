from game.scrabblegame import ScrabbleGame

class Main_Menu():
    def __init__(self):
        self.scrabble = None

    def welcome_message(self):
        print("--------------------------------------------------------------------------------------------")
        print("------------------------------------Bienvenido a Scrabble-------------------------------------")

    def get_player_count(self):
        while True:
            try:
                player_count = int(input("Introduce el numero de jugadores (1-3): "))
                if 1 <= player_count <= 3:
                    return player_count
                else:
                    print("Numero de jugadores invalido. Porfavor ingrece un numero entre 1 y 3")
            except ValueError:
                print("Valor invalido. Por favor ingresa un NUMERO VALIDO")

    def show_game_options(self):
        print("----------------------------------------Tabla de Scrabble-----------------------------------------")
        print(self.scrabble.board)
        print("-------------------------------------------Opciones---------------------------------------------")
        print("Preciona 1 para poner palabra")
        print("Preciona 2 para cambiar tus letras")
        print("Preciona 3 para cambiar todas tus letras")
        print("Preciona 4 para saltear turno")
        print("Preciona 5 para terminar el juego")
        print("-----------------------------------------------------------------------------------------------")
        print(self.scrabble.get_current_player())

    def get_word_input(self):
        while True:
            word = input("Ingresa tu palabra: ").upper()
            if word.isalpha():
                return word
            else:
                print("Palabra invalida.Por favor ingresa solo caracteres alfabeticos.")

    def get_coordinates(self):
        while True:
            try:
                x = int(input("ingresa la posicion en eje X: "))
                y = int(input("ingresa la posicion en eje Y: "))
                return x, y
            except ValueError:
                print("Valor invalido. Por favor ingrese una coordenada valida.")

    def get_orientation(self):
        while True:
            orientation = input("Que orientacion va a tener la palabra (H/V): ").upper()
            if orientation in ['H', 'V']:
                return orientation
            else:
                print("Valor invalido. por favor ingresa 'H' para horizontal o 'V' para vertical.")

    def handle_user_input(self, option):
        if option == 1:
            word = self.get_word_input()
            x, y = self.get_coordinates()
            orientation = self.get_orientation()
            if self.scrabble.round <= 2:
                self.scrabble.play_first_round(word, (x, y), orientation)
            else:
                self.scrabble.play(word, (x, y), orientation)
        elif option == 2:
            tiles_to_exchange_indices = input("Ingresa el indice de la letra que quieras cambiar (comma-separados): ").split(',')
            old_tiles_indices = [int(index.strip()) for index in tiles_to_exchange_indices]
            self.exchanged_tiles = self.scrabble.exchange_tiles(old_tiles_indices)
            print("Letras cambiadas: ", self.exchanged_tiles)
        elif option == 3:
            print('Bien, cambaindo todas tus letras')
            exchanged_tiles = self.scrabble.exchange_all_tiles()
            print("Letras cambiadas: ", exchanged_tiles)
        elif option == 4:
            print("Entendido, pasando al siguiente jugador...")
            self.scrabble.next_turn()
        elif option == 5:
            print('MUCHAS GRACIAS POR JUAGAR SCRABBLE')
            exit()
        else:
            print("Valor invalido por favor ingresar uno correcto.")

    def Begin_game(self):
        self.welcome_message()
        player_count = self.get_player_count()
        self.scrabble = ScrabbleGame(total_players=player_count)

        while self.scrabble.is_playing():
            self.scrabble.next_turn()
            self.scrabble.start_game()

            while True:
                self.show_game_options()
                option = int(input("Elige tus opciones: "))
                self.handle_user_input(option)
                
    