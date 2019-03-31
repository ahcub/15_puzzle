from io import StringIO

from fifteen_puzzle.fifteen_puzzle import FifteenPuzzle
from tests.utils import ResponsesGen


def test_play(mocker):
    mocker.patch('fifteen_puzzle.model.shuffle')
    responses_gen = ResponsesGen(['', '12', '12'])
    io = StringIO()
    fp = FifteenPuzzle(responses_gen, io.write)
    mock = mocker.patch.object(fp.model, 'tiles_sorted', )
    mock.side_effect = ResponsesGen([False, False, True])
    fp.play()

    expected_input_messages = ['press enter to start the game',
                               'enter tile_number number to move: ',
                               'enter tile_number number to move: ']
    assert responses_gen.input_messages == expected_input_messages
    expected_output = (' 1  2  3  4\n 5  6  7  8\n 9 10 11 12\n13 14 15   '
                       ' 1  2  3  4\n 5  6  7  8\n 9 10 11   \n13 14 15 12'
                       ' 1  2  3  4\n 5  6  7  8\n 9 10 11 12\n13 14 15   '
                       'CONGRATULATIONS!'
                       'The tiles are ordered!')
    assert io.getvalue() == expected_output


def test_read_tile_number_to_move(mocker):
    mocker.patch('fifteen_puzzle.model.shuffle')
    responses_gen = ResponsesGen(['15', '11', 'aaa', '', '1'])
    io = StringIO()
    fp = FifteenPuzzle(responses_gen, io.write)
    assert fp.read_tile_number_to_move() == 15
    assert fp.read_tile_number_to_move() == 11
    assert fp.read_tile_number_to_move() == -1
    assert fp.read_tile_number_to_move() == -1
    assert fp.read_tile_number_to_move() == 1


def test_make_a_move(mocker):
    mocker.patch('fifteen_puzzle.model.shuffle')
    responses_gen = ResponsesGen(['15', '11', 'aaa', '1'])
    io = StringIO()
    fp = FifteenPuzzle(responses_gen, io.write)
    fp.make_a_move()
    fp.make_a_move()
    fp.make_a_move()
    fp.make_a_move()

    expected_input_messages = ['enter tile_number number to move: '] * 4
    assert responses_gen.input_messages == expected_input_messages
    expected_game_field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 12, 13, 14, 11, 15]
    expected_rows_col_map = {
        1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3),
        5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (1, 3),
        9: (2, 0), 10: (2, 1), 11: (3, 2), 12: (2, 3),
        13: (3, 0), 14: (3, 1), 15: (3, 3), 16: (2, 2),
    }

    expected_tiles_pos = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9,
                          11: 14, 12: 11, 13: 12, 14: 13, 15: 15, 16: 10}

    assert fp.model.game_field == expected_game_field
    assert fp.model.tiles_rows_cols_map == expected_rows_col_map
    assert fp.model.tiles_game_field_pos == expected_tiles_pos

    expected_output = (
        '\ninvalid input, please use a number from 1 to 15\n'
        '\ninvalid move, please use a different tile_number number\n'
    )

    assert io.getvalue() == expected_output
