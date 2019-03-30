from fifteen_puzzle.constants import END_TILE_NUM, GAME_FIELD_WIDTH, EMPTY_TILE_NUM


class View:
    def __init__(self, output_writer):
        self.output_writer = output_writer

    def print_game_field(self, game_field):
        str_rows = []
        for row_start in range(0, END_TILE_NUM, GAME_FIELD_WIDTH):
            row_end = row_start + GAME_FIELD_WIDTH
            game_field_row = game_field[row_start:row_end]
            row_tiles = []
            for tile in game_field_row:
                if tile == EMPTY_TILE_NUM:
                    row_tiles.append('  ')
                else:
                    row_tiles.append('{:2d}'.format(tile))
            str_rows.append(' '.join(row_tiles))
        self.write_message('\n'.join(str_rows))

    def write_message(self, message, *args):
        self.output_writer(message.format(*args))

    def print_error(self, error_message, *args):
        self.write_message('\n{}\n'.format(error_message), *args)
