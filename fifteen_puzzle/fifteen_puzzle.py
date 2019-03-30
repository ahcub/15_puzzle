from fifteen_puzzle.constants import INVALID_TILE_NUMBER, START_TILE_NUM, END_TILE_NUM
from fifteen_puzzle.model import Model
from fifteen_puzzle.view import View


class FifteenPuzzle:
    def __init__(self, input_reader, output_writer):
        self.model = Model()
        self.view = View(output_writer)
        self.input_reader = input_reader

    def play(self):
        self.read_user_input('press enter to start the game')
        while not self.model.tiles_sorted():
            self.view.print_game_field(self.model.game_field)
            self.make_a_move()
        self.view.print_game_field(self.model.game_field)
        self.view.write_message('CONGRATULATIONS!')
        self.view.write_message('The tiles are ordered!')

    def read_user_input(self, additional_message=''):
        return self.input_reader(additional_message)

    def make_a_move(self):
        tile_number = self.read_tile_number_to_move()
        if tile_number == INVALID_TILE_NUMBER:
            self.view.print_error('invalid input, please use a number from {} to {}',
                                  START_TILE_NUM, END_TILE_NUM)
        else:
            if self.model.tile_number_is_valid(tile_number):
                self.model.move_tile(tile_number)
            else:
                self.view.print_error('invalid move, please use a different tile_number number')

    def read_tile_number_to_move(self):
        user_input = self.read_user_input('enter tile_number number to move: ')
        if user_input.isdigit():
            tile_number = int(user_input)
            if tile_number < START_TILE_NUM or tile_number > END_TILE_NUM:
                tile_number = INVALID_TILE_NUMBER
        else:
            tile_number = INVALID_TILE_NUMBER
        return tile_number
