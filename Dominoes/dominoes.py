import random

n = 7
all_pieces = []
for i in range(n):
    for j in range(n):
        temp1 = [i, j]
        temp2 = [j, i]
        if temp1 not in all_pieces and temp2 not in all_pieces:
            all_pieces.append([i, j])
while True:
    stock_pieces = random.sample(all_pieces, 14)
    remaining = [piece for piece in all_pieces if piece not in stock_pieces]
    computer_pieces = random.sample(remaining, 7)
    player_pieces = [piece for piece in remaining if piece not in computer_pieces]
    double_player = [piece for piece in player_pieces if piece[0] == piece[1]]
    double_computer = [piece for piece in computer_pieces if piece[0] == piece[1]]
    if len(double_computer) == len(double_player) == 0:
        continue
    elif len(double_computer) == 0:
        max_player = max(double_player)
        snake = [max_player]
        status = 'computer'
        del player_pieces[player_pieces.index(snake[0])]
    elif len(double_player) == 0:
        max_computer = max(double_computer)
        snake = [max_computer]
        status = 'player'
        del computer_pieces[computer_pieces.index(snake[0])]
    else:
        max_player = max(double_player)
        max_computer = max(double_computer)
        if max_computer > max_player:
            snake = [max_computer]
            status = 'player'
            del computer_pieces[computer_pieces.index(snake[0])]
        else:
            snake = [max_player]
            status = 'computer'
            del player_pieces[player_pieces.index(snake[0])]
    break


def snake_print(snake):
    print()
    if len(snake) < 7:
        for i in range(len(snake)):
            print(snake[i], end='')
        print()
    else:
        print(f'{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}')
    print()


def game_play(status, computer_pieces, player_pieces, stock_pieces, snake):
    def turn_check_computer(turn, pieces, snake, repeat, computer_pieces):
        orient = False
        while True:
            repeat = 1 + repeat
            if turn == 0:
                return turn, pieces, snake, orient
            elif turn < 0:
                temp = pieces[abs(turn) - 1]
                if temp[1] == snake[0][0]:
                    return turn, pieces, snake, orient
                elif temp[0] == snake[0][0]:
                    orient = True
                    return turn, pieces, snake, orient
                else:
                    turn, computer_pieces = ai_turn(snake, computer_pieces, repeat)
                    continue
            else:
                temp = pieces[turn - 1]
                if temp[0] == snake[-1][1]:
                    return turn, pieces, snake, orient
                elif temp[1] == snake[-1][1]:
                    orient = True
                    return turn, pieces, snake, orient
                else:
                    turn, computer_pieces = ai_turn(snake, computer_pieces, repeat)
                    continue

    def turn_check_player(snake):
        while True:
            turn = input()
            try:
                turn = int(turn)
                if -len(player_pieces) <= turn <= len(player_pieces):
                    pieces = player_pieces.copy()
                    orient = False
                    while True:
                        if turn == 0:
                            return turn, pieces, snake, orient
                        elif turn < 0:
                            temp = pieces[abs(turn) - 1]
                            if temp[1] == snake[0][0]:
                                return turn, pieces, snake, orient
                            elif temp[0] == snake[0][0]:
                                orient = True
                                return turn, pieces, snake, orient
                            else:
                                print('Illegal move. Please try again.')
                                break
                        else:
                            temp = pieces[turn - 1]
                            if temp[0] == snake[-1][1]:
                                return turn, pieces, snake, orient
                            elif temp[1] == snake[-1][1]:
                                orient = True
                                return turn, pieces, snake, orient
                            else:
                                print('Illegal move. Please try again.')
                                break
                    continue
                else:
                    print('Invalid input. Please try again.')
                    continue
            except Exception:
                print('Invalid input. Please try again.')
                continue

    while True:
        if status == 'computer':
            print('Status: Computer is about to make a move. Press Enter to continue...')
            if input() == '':
                pass
            repeat = 0
            turn, computer_pieces = ai_turn(snake, computer_pieces, repeat)
            pieces = computer_pieces.copy()
            turn, pieces, snake, orient = turn_check_computer(turn, pieces, snake, repeat, computer_pieces)
            break
        else:
            print("Status: It's your turn to make a move. Enter your command.")
            turn, pieces, snake, orient = turn_check_player(snake)
            break
    if turn < 0:
        turn = turn + 1
        if not orient:
            snake.insert(0, pieces[abs(turn)])
        else:
            snake.insert(0, pieces[abs(turn)][::-1])
        del pieces[abs(turn)]
    elif turn > 0:
        turn = turn - 1
        if not orient:
            snake.append(pieces[turn])
        else:
            snake.append(pieces[turn][::-1])
        del pieces[turn]
    else:
        try:
            pieces.append(random.choice(stock_pieces))
            del stock_pieces[stock_pieces.index(pieces[-1])]
        except Exception:
            pass
    if status == 'player':
        status = 'computer'
        player_pieces = pieces.copy()
    else:
        status = 'player'
        computer_pieces = pieces.copy()
    return status, computer_pieces, player_pieces, stock_pieces, snake


def check_status(computer_pieces, player_pieces, snake):
    win = False
    if len(computer_pieces) == 0:
        print('Status: The game is over. The computer won!')
        win = True
    elif len(player_pieces) == 0:
        print('Status: The game is over. You won!')
        win = True
    elif snake[0][0] == snake[-1][1]:
        temp = snake[0][0]
        count = 0
        for i in snake:
            count = count + i.count(temp)
        if count >= 8:
            win = True
            print("Status: The game is over. It's a draw!")
    return win


def ai_turn(snake, computer_pieces, repeat):
    scores = []
    for i in range(n):
        count = 0
        for piece in snake:
            count = count + piece.count(i)
        for piece in computer_pieces:
            count = count + piece.count(i)
        scores.append(count)
    cp_score = []
    for piece in computer_pieces:
        cp_score.append(scores[piece[0]] + scores[piece[1]])
    computer_pieces = [x for x, _ in sorted(zip(computer_pieces, cp_score))]
    if repeat % 2 == 0:
        turn = len(computer_pieces) - repeat // 2
    else:
        turn = -(len(computer_pieces) - repeat // 2)
    return turn, computer_pieces

while True:
    print('=' * 70)
    print('Stock size:', len(stock_pieces))
    print('Computer pieces:', len(computer_pieces))

    snake_print(snake)

    print('Your pieces:')
    for i in range(len(player_pieces)):
        print(f"{i+1}:{player_pieces[i]}")
    print()

    win = check_status(computer_pieces, player_pieces, snake)
    if win:
        break
    else:
        status, computer_pieces, player_pieces, stock_pieces, snake = game_play(status, computer_pieces, player_pieces, stock_pieces, snake)
