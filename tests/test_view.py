from io import StringIO

from fifteen_puzzle.view import View
from tests.utils import ResponsesGen


def test_write_message():
    io = StringIO()
    view = View(None, io.write)
    view.write_message('test_message1')
    assert io.getvalue() == 'test_message1'
    view.write_message('test_message2')
    assert io.getvalue() == 'test_message1test_message2'
    view.write_message('test_message3 {}, {}', 'arg1', 'arg2')
    assert io.getvalue() == 'test_message1test_message2test_message3 arg1, arg2'


def test_print_error():
    io = StringIO()
    view = View(None, io.write)
    view.print_error('erorr_message_1')
    assert io.getvalue() == '\nerorr_message_1\n'
    view.write_message('test_message')
    view.print_error('erorr_message_2')
    assert io.getvalue() == '\nerorr_message_1\ntest_message\nerorr_message_2\n'


def test_print_game_field():
    io = StringIO()
    view = View(None, io.write)
    game_field = [1, 2, 3, 10, 5, 6, 7, 8, 9, 4, 16, 12, 13, 14, 11, 15]
    view.print_game_field(game_field)
    expected_value = ' 1  2  3 10\n 5  6  7  8\n 9  4    12\n13 14 11 15'
    assert io.getvalue() == expected_value


def test_read_user_input():
    io = StringIO()
    responses_gen = ResponsesGen('')
    fp = View(responses_gen, io.write)
    fp.read_user_input()
    assert responses_gen.input_messages == ['']
    fp.read_user_input('test input message:')
    assert responses_gen.input_messages == ['', 'test input message:']
