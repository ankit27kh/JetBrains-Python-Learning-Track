class KnightGame:

    def __init__(self):
        self.dim_x = 0
        self.dim_y = 0
        self.area = 0
        self.num_moves = 1
        self.solution = False
        self.visited_squares = []
        self.current_square = [0, 0]
        self.board_dimension()

    def draw_board(self, x, y):
        cell_size = len(str(self.area))
        under_symbol = '_' * cell_size
        self.current_square = [x, y]
        possibilities = self.possible_moves(self.current_square)
        print(' ' * len(str(self.dim_y)), end='')
        print('-' * (self.dim_x * (cell_size + 1) + 3))
        for j in range(self.dim_y, 0, -1):
            print(f'{j}'.rjust(len(str(self.dim_y))) + '|', end='')
            for i in range(1, self.dim_x + 1):
                if [i, j] in self.visited_squares:
                    print(' ' * cell_size + '*', end='')
                elif [i, j] == self.current_square:
                    print(' ' * cell_size + 'X', end='')
                elif [i, j] in possibilities:
                    print(' ' * cell_size + f'{self.count_moves(i, j)}', end='')
                else:
                    print(' ' + f'{under_symbol}', end='')
            print(' |')
        print(' ' * len(str(self.dim_y)), end='')
        print('-' * (self.dim_x * (cell_size + 1) + 3))
        print(' ' * (len(str(self.dim_y)) + 1), end='')
        for i in range(1, self.dim_x + 1):
            print(f'{i}'.rjust(cell_size + 1), end='')
        print()
        self.visited_squares.append(self.current_square)
        self.next_step(possibilities)

    def next_step(self, allowed_moves):
        if allowed_moves:
            move = input('Enter your next move: ').split()
            if [int(move[0]), int(move[1])] in allowed_moves:
                self.num_moves = self.num_moves + 1
                self.draw_board(int(move[0]), int(move[1]))
            else:
                print('Invalid move! ', end='')
                self.next_step(allowed_moves)
        else:
            if self.num_moves == self.area:
                print('What a great tour! Congratulations!')
            else:
                print('No more possible moves!')
                print(f'Your knight visited {self.num_moves} squares')

    def possible_moves(self, position):
        x = position[0]
        y = position[1]
        x_poss = [x-1, x+1, x-2, x+2, x-2, x+2, x-1, x+1]
        y_poss = [y+2, y+2, y+1, y+1, y-1, y-1, y-2, y-2]
        temp = [[i, j] for i, j in zip(x_poss, y_poss) if i in range(1, self.dim_x + 1) and j in range(1, self.dim_y + 1)]
        for i in self.visited_squares:
            if i in temp:
                temp.remove(i)
        return temp

    def count_moves(self, x, y):
        count = 0
        if x - 1 in range(1, self.dim_x + 1) and y + 2 in range(1, self.dim_y + 1) and [x-1, y+2] not in self.visited_squares:
            count = count + 1
        if x + 1 in range(1, self.dim_x + 1) and y + 2 in range(1, self.dim_y + 1) and [x+1, y+2] not in self.visited_squares:
            count = count + 1
        if x - 2 in range(1, self.dim_x + 1) and y + 1 in range(1, self.dim_y + 1) and [x-2, y+1] not in self.visited_squares:
            count = count + 1
        if x + 2 in range(1, self.dim_x + 1) and y + 1 in range(1, self.dim_y + 1) and [x+2, y+1] not in self.visited_squares:
            count = count + 1
        if x - 2 in range(1, self.dim_x + 1) and y - 1 in range(1, self.dim_y + 1) and [x-2, y-1] not in self.visited_squares:
            count = count + 1
        if x + 2 in range(1, self.dim_x + 1) and y - 1 in range(1, self.dim_y + 1) and [x+2, y-1] not in self.visited_squares:
            count = count + 1
        if x - 1 in range(1, self.dim_x + 1) and y - 2 in range(1, self.dim_y + 1) and [x-1, y-2] not in self.visited_squares:
            count = count + 1
        if x + 1 in range(1, self.dim_x + 1) and y - 2 in range(1, self.dim_y + 1) and [x+1, y-2] not in self.visited_squares:
            count = count + 1
        return count - 1
    
    def board_dimension(self):
        try:
            x, y = input("Enter your board dimensions: ").split()
            x = int(x)
            y = int(y)
            if x <= 0 or y <= 0:
                print('Invalid dimension!')
                self.board_dimension()
            else:
                self.dim_x = x
                self.dim_y = y
                self.area = x * y
                self.initial_position()
        except ValueError:
            print('Invalid dimension!')
            self.board_dimension()

    def initial_position(self):
        try:
            i, j = input("Enter the knight's starting position: ").split()
            i = int(i)
            j = int(j)
            if i in range(1, self.dim_x + 1) and j in range(1, self.dim_y + 1):
                self.puzzle_try(i, j)
            else:
                print('Invalid position!')
                self.initial_position()
        except ValueError:
            print('Invalid position!')
            self.initial_position()

    def puzzle_try(self, ini_x, ini_y):
        try_ = input('Do you want to try the puzzle? (y/n): ')
        if try_ not in ['y', 'n']:
            print('Invalid option')
            self.puzzle_try(ini_x, ini_y)
        else:
            self.solution, result = self.get_solution(ini_x, ini_y, try_)
            if try_ == 'n':
                if not self.solution:
                    print('No solution exists!')
                else:
                    self.draw_final(result)
            else:
                if self.area > 25:
                    self.visited_squares = []
                    self.draw_board(ini_x, ini_y)
                elif self.solution:
                    self.visited_squares = []
                    self.draw_board(ini_x, ini_y)
                else:
                    print('No solution exists!')

    def get_solution(self, ini_x, ini_y, try_):
        moves_made = {1: [ini_x, ini_y]}
        count = 1
        times = -1
        forks = []
        while True:
            moves_possible = self.possible_moves(moves_made[count])
            next_moves_count = [self.count_moves(i, j) for [i, j] in moves_possible]
            if count == self.dim_x * self.dim_y and try_ == 'n':
                return True, moves_made
            elif count == self.dim_x * self.dim_y:
                return True, moves_made
            if not forks and not next_moves_count:
                return False, moves_made
            elif len(next_moves_count) == 0:
                for i in range(forks[times][0], len(moves_made) + 1):
                    temp = moves_made.pop(i)
                self.visited_squares = forks[times][2]
                moves_possible = self.possible_moves(moves_made[forks[times][0] - 1])
                next_moves_count = [self.count_moves(i, j) for [i, j] in moves_possible]
                min_count = min(next_moves_count)
                if min_count == -1:
                    return False, moves_made
                moves_possible.remove(moves_possible[min_count])
                next_moves_count.remove(min_count)
                count = forks[times][0] - 1
            else:
                min_count = min(next_moves_count)
                if min_count == 0 and len(next_moves_count) != 1:
                    next_moves_count.remove(0)
                    min_count = min(next_moves_count)
            if next_moves_count.count(min_count) == 1:
                count = count + 1
                self.visited_squares.append(moves_made[count - 1])
                moves_made[count] = moves_possible[next_moves_count.index(min_count)]
                continue
            else:
                times = times + 1
                count = count + 1
                copy = self.visited_squares.copy()
                forks.append([count, min_count, copy])
                self.visited_squares.append(moves_made[count - 1])
                moves_made[count] = moves_possible[next_moves_count.index(min_count)]
                continue

    def draw_final(self, moves_made):
        print("Here's the solution!")
        cell_size = len(str(self.area))
        print(' ' * len(str(self.dim_y)), end='')
        print('-' * (self.dim_x * (cell_size + 1) + 3))
        for j in range(self.dim_y, 0, -1):
            print(f'{j}'.rjust(len(str(self.dim_y))) + '|', end='')
            for i in range(1, self.dim_x + 1):
                print(f'{list(moves_made.keys())[list(moves_made.values()).index([i, j])]}'.rjust(cell_size + 1), end='')
            print(' |')
        print(' ' * len(str(self.dim_y)), end='')
        print('-' * (self.dim_x * (cell_size + 1) + 3))
        print(' ' * (len(str(self.dim_y)) + 1), end='')
        for i in range(1, self.dim_x + 1):
            print(f'{i}'.rjust(cell_size + 1), end='')
        print()


game = KnightGame()
