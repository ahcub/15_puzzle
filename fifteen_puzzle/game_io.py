from fifteen_puzzle.constants import END_TILE_NUM, GAME_FIELD_WIDTH, EMPTY_TILE_NUM


class GameIO:
    def __init__(self, input_reader, output_writer):
        self.input_reader = input_reader
        self.output_writer = output_writer

    def read_user_input(self, additional_message=''):
        return self.input_reader(additional_message)

    def write_message(self, message, *args):
        self.output_writer(message.format(*args))

    def print_error(self, error_message, *args):
        self.write_message('\n{}\n'.format(error_message), *args)

    def print_game_field(self, game_field):
        for row_start in range(0, END_TILE_NUM, GAME_FIELD_WIDTH):
            row_end = row_start + GAME_FIELD_WIDTH
            game_field_row = game_field[row_start:row_end]
            row_tiles = []
            for tile in game_field_row:
                if tile == EMPTY_TILE_NUM:
                    row_tiles.append('  ')
                else:
                    row_tiles.append('{:2d}'.format(tile))
            self.write_message(' '.join(row_tiles))
