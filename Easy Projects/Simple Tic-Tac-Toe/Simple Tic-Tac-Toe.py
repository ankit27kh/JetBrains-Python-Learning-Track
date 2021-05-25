state = '_________'
state = list(state)
turn = 1
game_finish = 0


def draw(state):
    print('-' * 9)
    print('| ' + state[0], state[1], state[2] + ' |')
    print('| ' + state[3], state[4], state[5] + ' |')
    print('| ' + state[6], state[7], state[8] + ' |')
    print('-' * 9)


def enter_coordinates_new_state(state, turn):
    check1 = 0
    check2 = 0
    check3 = 0
    while True:
        temp = input('Enter the coordinates: ')
        x, y = temp.split()
        try:
            x = int(x)
            y = int(y)
            check2 = 1
        except:
            print('You should enter numbers!')
            continue
        if x not in [1, 2, 3] or y not in [1, 2, 3]:
            print('Coordinates should be from 1 to 3!')
            continue
        else:
            check1 = 1
        new = 3 * (x-1) + (y-1)
        if state[new] != '_':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            if turn % 2 == 0:
                state[new] = 'O'
            else:
                state[new] = 'X'
            check3 = 1
            turn = turn + 1
        if check1 + check2 + check3 == 3:
            break
    return state, turn


def game_state(state, game_finish):
    count_X = state.count('X')
    count_O = state.count('O')
    count_blank = state.count('_')
    row1 = [state[0], state[1], state[2]]
    row2 = [state[3], state[4], state[5]]
    row3 = [state[6], state[7], state[8]]
    col1 = [state[0], state[3], state[6]]
    col2 = [state[1], state[4], state[7]]
    col3 = [state[2], state[5], state[8]]
    dia1 = [state[0], state[4], state[8]]
    dia2 = [state[2], state[4], state[6]]
    X_win = 0
    O_win = 0

    if row1 == ['X', 'X', 'X'] or row2 == ['X', 'X', 'X'] or row3 == ['X', 'X', 'X']:
        X_win = 1
    elif col1 == ['X', 'X', 'X'] or col2 == ['X', 'X', 'X'] or col3 == ['X', 'X', 'X']:
        X_win = 1
    elif dia1 == ['X', 'X', 'X'] or dia2 == ['X', 'X', 'X']:
        X_win = 1
    if row1 == ['O', 'O', 'O'] or row2 == ['O', 'O', 'O'] or row3 == ['O', 'O', 'O']:
        O_win = 1
    elif col1 == ['O', 'O', 'O'] or col2 == ['O', 'O', 'O'] or col3 == ['O', 'O', 'O']:
        O_win = 1
    elif dia1 == ['O', 'O', 'O'] or dia2 == ['O', 'O', 'O']:
        O_win = 1
    if X_win == 1:
        draw(state)
        print('X wins')
        game_finish = 1
    elif O_win == 1:
        draw(state)
        print('O wins')
        game_finish = 1
    elif count_blank == 0:
        draw(state)
        print('Draw')
        game_finish = 1
    else:
        game_finish = 0
    return game_finish


draw(state)
state, turn = enter_coordinates_new_state(state, turn)


def play_game(state, turn, game_finish):
    while game_finish == 0:
        draw(state)
        state, turn = enter_coordinates_new_state(state, turn)
        game_finish = game_state(state, game_finish)

play_game(state, turn, game_finish)