from fifteen_puzzle.console_io import ConsoleIO
from fifteen_puzzle.constants import (SORTED_TILES_ARRAY, INVALID_TILE_NUMBER, START_TILE_NUM,
                                      END_TILE_NUM)
from fifteen_puzzle.controller import GameController


class FifteenPuzzle:
    def __init__(self):
        self.io = ConsoleIO(input, print)
        self.gc = GameController(self.io)

    def play(self):
        self.io.read_user_input('press enter to start the game')
        while not self.tiles_sorted():
            self.io.print_game_field(self.gc.game_field)
            self.make_a_move()
        self.io.print_game_field(self.gc.game_field)
        self.io.write_message('CONGRATULATIONS!')
        self.io.write_message('The tiles are ordered!')

    def tiles_sorted(self):
        return self.gc.game_field == SORTED_TILES_ARRAY

    def make_a_move(self):
        tile_number = self.gc.read_tile_number_to_move()
        if tile_number == INVALID_TILE_NUMBER:
            self.io.print_error('invalid input, please use a number from {} to {}',
                                START_TILE_NUM, END_TILE_NUM)
        else:
            if self.gc.tile_number_is_valid(tile_number):
                self.gc.move_tile(tile_number)
            else:
                self.io.print_error('invalid move, please use a different tile_number number')
