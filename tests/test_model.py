import pytest

from fifteen_puzzle.constants import SORTED_TILES_ARRAY
from fifteen_puzzle.model import Model


def test_model_init():
    m = Model()
    assert m.game_field != SORTED_TILES_ARRAY


@pytest.mark.parametrize('test_input,expected', [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], True),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 15], False),
    ([11, 2, 10, 7, 5, 14, 4, 8, 9, 3, 1, 13, 12, 6, 16, 15], False),
])
def test_tiles_sorted(test_input, expected):
    game_instance = Model()
    game_instance.game_field = test_input
    assert game_instance.tiles_sorted() is expected


def test_generate_tiles_possition_map():
    game_field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    expected_output = {
        1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3),
        5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (1, 3),
        9: (2, 0), 10: (2, 1), 11: (2, 2), 12: (2, 3),
        13: (3, 0), 14: (3, 1), 15: (3, 2), 16: (3, 3),
    }
    assert Model.generate_tiles_possition_map(game_field) == expected_output


def test_exchange_collection_values():
    game_field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    expected_game_field = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    Model.exchange_collection_values(game_field, 2, 3)
    assert game_field == expected_game_field


def test_move_tile(mocker):
    mocker.patch('fifteen_puzzle.model.shuffle')
    m = Model()
    m.move_tile(15)
    m.move_tile(11)
    expected_game_field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 12, 13, 14, 11, 15]
    expected_rows_col_map = {
        1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3),
        5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (1, 3),
        9: (2, 0), 10: (2, 1), 11: (3, 2), 12: (2, 3),
        13: (3, 0), 14: (3, 1), 15: (3, 3), 16: (2, 2),
    }

    expected_tiles_pos = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9,
                          11: 14, 12: 11, 13: 12, 14: 13, 15: 15, 16: 10}

    assert m.game_field == expected_game_field
    assert m.tiles_rows_cols_map == expected_rows_col_map
    assert m.tiles_game_field_pos == expected_tiles_pos


def test_tile_number_is_valid(mocker):
    mocker.patch('fifteen_puzzle.model.shuffle')
    m = Model()
    assert m.tile_number_is_valid(15) is True
    assert m.tile_number_is_valid(12) is True
    assert m.tile_number_is_valid(11) is False
    assert m.tile_number_is_valid(1) is False
    m.move_tile(15)
    assert m.tile_number_is_valid(11) is True
