from copy import deepcopy
from random import shuffle

from fifteen_puzzle.constants import (SORTED_TILES_ARRAY, GAME_FIELD_HEIGHT, GAME_FIELD_WIDTH,
                                      EMPTY_TILE_NUM)


class Model:
    def __init__(self):
        self.game_field = deepcopy(SORTED_TILES_ARRAY)
        shuffle(self.game_field)
        self.tiles_rows_cols_map = self.generate_tiles_possition_map(self.game_field)
        self.tiles_game_field_pos = {tile: index for index, tile in enumerate(self.game_field)}

    @staticmethod
    def generate_tiles_possition_map(game_field):
        tiles_pos_map = {}
        for game_filed_pos, tile_number in enumerate(game_field):
            row_pos = game_filed_pos // GAME_FIELD_HEIGHT
            col_pos = game_filed_pos % GAME_FIELD_WIDTH
            tiles_pos_map[tile_number] = (row_pos, col_pos)
        return tiles_pos_map

    def tiles_sorted(self):
        return self.game_field == SORTED_TILES_ARRAY

    def tile_number_is_valid(self, tile_number):
        tile_row, tile_col = self.tiles_rows_cols_map[tile_number]
        empty_tile_row, empty_tile_col = self.tiles_rows_cols_map[EMPTY_TILE_NUM]
        if tile_row == empty_tile_row:
            if tile_col in [empty_tile_col - 1, empty_tile_col + 1]:
                return True
        if tile_col == empty_tile_col:
            if tile_row in [empty_tile_row - 1, empty_tile_row + 1]:
                return True

        return False

    def move_tile(self, tile_number):
        self.exchange_collection_values(self.tiles_rows_cols_map, tile_number, EMPTY_TILE_NUM)
        self.exchange_collection_values(self.game_field, self.tiles_game_field_pos[tile_number],
                                        self.tiles_game_field_pos[EMPTY_TILE_NUM])
        self.exchange_collection_values(self.tiles_game_field_pos, tile_number, EMPTY_TILE_NUM)

    @staticmethod
    def exchange_collection_values(collection, id_1, id_2):
        collection[id_1], collection[id_2] = collection[id_2], collection[id_1]
