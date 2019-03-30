import pytest

from fifteen_puzzle.model import Model


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

