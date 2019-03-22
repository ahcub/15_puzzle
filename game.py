from random import shuffle

DESIRED_ARRAY = list(range(1, 17))
EMPTY_TILE = 16


def game():
    print('press enter to start the game')
    input()
    game_field = list(range(1, 17))
    shuffle(game_field)
    tiles_pos_map = {tile: (i // 4, i % 4, i) for i, tile in enumerate(game_field)}
    while game_field != DESIRED_ARRAY:
        print_game_field(game_field)
        try:
            tile = int(input('enter tile number to move: '))
            if tile < 1 or tile > 15:
                raise ValueError('invalid value range')
        except ValueError:
            print('\nplease input numbers from 1 to 15\n')
            continue
        tile_x, tile_y, tile_pos = tiles_pos_map[tile]
        empty_tile_x, empty_tile_y, empty_tile_pos = tiles_pos_map[EMPTY_TILE]
        if check_if_move_is_valid(tile_x, tile_y, empty_tile_x, empty_tile_y):
            tiles_pos_map[tile], tiles_pos_map[EMPTY_TILE] = tiles_pos_map[EMPTY_TILE], tiles_pos_map[tile]
            game_field[tile_pos], game_field[empty_tile_pos] = game_field[empty_tile_pos], game_field[tile_pos]
        else:
            print('\ninvalid move, please use a different tile number\n')
    print('CONGRATULATIONS!\nThe tiles are ordered!')
    print_game_field(game_field)


def print_game_field(game_field):
    for i in range(0, 16, 4):
        print(' '.join('{:2d}'.format(el) if el != 16 else '  ' for el in game_field[i:i+4]))


def check_if_move_is_valid(tile_x, tile_y, empty_tile_x, empty_tile_y):
    return (tile_x == empty_tile_x and (tile_y == empty_tile_y - 1 or tile_y == empty_tile_y + 1)) or \
           (tile_y == empty_tile_y and (tile_x == empty_tile_x - 1 or tile_x == empty_tile_x + 1))


if __name__ == '__main__':
    game()
