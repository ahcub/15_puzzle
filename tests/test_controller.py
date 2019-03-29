import pytest

from fifteen_puzzle.controller import GameController
from fifteen_puzzle.fifteen_puzzle import check_if_move_is_valid


@pytest.mark.parametrize("test_input,expected", [
    ((0, 0, 0, 1), True),
    ((0, 0, 1, 1), False),
    ((0, 1, 1, 1), True),
    ((2, 2, 2, 1), True),
    ((2, 2, 1, 2), True),
    ((3, 2, 1, 2), False),
])
def test_check_if_move_is_valid(test_input, expected):
    assert check_if_move_is_valid(*test_input) == expected


def test_move_is_valid():
    game_contorller = GameController()