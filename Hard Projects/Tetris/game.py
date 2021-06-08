import random


class Tetris:

    def __init__(self):
        print("Press 'w' to rotate the piece, 'a' to move left, 'd' to move right and enter to move down.")
        print("Press 'p' to get a new piece once the last piece is fixed.")
        print("Press 'b' to break full lines from the bottom of the board.")
        print("Currently, to play correctly, you need to fill from the bottom up without leaving any space.")
        self.size = input("Enter size of the board (columns (> 10) rows (> 10): ").split()
        self.size = [int(n) for n in self.size]
        self.columns = self.size[0]
        self.rows = self.size[1]
        self.start = False
        self.score = 0
        self.position = 0
        self.fixed_blocks = []
        self.ban_blocks = []
        self.reference = {"I": 0, "S": 1, "Z": 2, 'L': 3, "J": 4, "O": 5, "T": 6}
        self.initial_piece = random.choice(list(self.reference.keys()))
        self.blocks()

    def ask_command(self):
        if not self.start:
            self.show_blocks()
        else:
            command = input()
            if command == 'exit':
                self.exit()
            elif command == 'p':
                self.initial_piece = random.choice(list(self.reference.keys()))
                self.position = 0
                self.blocks(False)
                self.show_blocks()
            else:
                self.show_blocks(command)

    def show_blocks(self, command=None):
        x = self.reference[self.initial_piece]
        selected = self.pieces[x]
        if not self.start:
            print()
            for i in range(self.rows):
                for j in range(self.columns):
                    if j == self.columns - 1:
                        print('-', end='')
                    else:
                        print('-', end=' ')
                print()
            self.start = True
        print(f"Score : {self.score}")
        orientation = self.next_move(command, selected)
        print()
        orientation.extend(self.fixed_blocks)
        orientation = set(orientation)
        if command == 'b':
            broken_blocks = sorted(self.fixed_blocks, reverse=True)
            number = len(broken_blocks)
            lines = number // self.columns
            while True:
                if broken_blocks[lines * self.columns - 1] == self.columns * self.rows - 1 - (lines * self.columns - 1):
                    break
                else:
                    lines = lines - 1
            self.score = lines ** 2 * 100
            orientation = [n for n in orientation if n < self.columns * (self.rows - lines)]
            self.fixed_blocks = [n for n in self.fixed_blocks if n in orientation]
            self.ban_blocks = [n + self.columns for n in self.fixed_blocks]
            orientation = [n + 10 for n in orientation]
        for i in range(self.rows):
            for j in range(self.columns):
                if self.columns * i + j in orientation:
                    if j == self.columns - 1:
                        print('0', end='')
                    else:
                        print('0', end=' ')
                else:
                    if j == self.columns - 1:
                        print('-', end='')
                    else:
                        print('-', end=' ')
            print()
        if any([True for n in self.fixed_blocks if n in range(self.columns)]):
            print('Game over!')
            self.exit()
        else:
            self.ask_command()

    def next_move(self, move, piece):
        if move is None:
            return piece[self.position].copy()
        if any([True for n in piece[self.position] if n in self.ban_blocks]):
            self.fixed_blocks = list(self.fixed_blocks)
            self.fixed_blocks.extend(piece[self.position])
            self.ban_blocks = [n - self.columns for n in self.fixed_blocks]
            self.fixed_blocks = set(self.fixed_blocks)
            self.ban_blocks = set(self.ban_blocks)
            return piece[self.position].copy()
        elif move == 'a':
            for i in range(len(piece)):
                next_piece = piece[i]
                if any([True for n in next_piece if n % self.columns == 0 or n >= self.columns * (self.rows - 1)]):
                    pass
                else:
                    next_piece = [n - 1 for n in next_piece]
                piece[i] = next_piece
        elif move == 'd':
            for i in range(len(piece)):
                next_piece = piece[i]
                if any([True for n in next_piece if n % self.columns == self.columns - 1 or n >= self.columns * (self.rows - 1)]):
                    pass
                else:
                    next_piece = [n + 1 for n in next_piece]
                piece[i] = next_piece
        elif move == 'w':
            if self.position + 1 < len(piece):
                self.position = self.position + 1
            else:
                self.position = 0
            if any([True for n in piece[self.position] if n >= self.columns * (self.rows - 1)]):
                self.position = self.position - 1
        for i in range(len(piece)):
            next_piece = piece[i]
            if any([True for n in next_piece if n >= self.columns * (self.rows - 1)]):
                pass
            else:
                next_piece = [n + self.columns for n in next_piece]
            piece[i] = next_piece
        if any([True for n in piece[self.position] if n >= self.columns * (self.rows - 1)]):
            self.fixed_blocks = list(self.fixed_blocks)
            self.fixed_blocks.extend(piece[self.position])
            self.ban_blocks = [n - self.columns for n in self.fixed_blocks]
            self.fixed_blocks = set(self.fixed_blocks)
            self.ban_blocks = set(self.ban_blocks)
        return piece[self.position].copy()

    def blocks(self, ask_command=True):
        rshift = int(self.columns / 2 - 5)
        self.I = [4, 14, 24, 34]
        self.S = [5, 4, 14, 13]
        self.Z = [4, 5, 15, 16]
        self.L = [4, 14, 24, 25]
        self.J = [5, 15, 25, 24]
        self.O = [4, 14, 15, 5]
        self.T = [4, 14, 24, 15]
        I_90 = [3, 4, 5, 6]
        self.rotated_I = [self.I, I_90]
        S_90 = [4, 14, 15, 25]
        self.rotated_S = [self.S, S_90]
        Z_90 = [5, 15, 14, 24]
        self.rotated_Z = [self.Z, Z_90]
        L_90 = [5, 15, 14, 13]
        L_180 = [4, 5, 15, 25]
        L_270 = [6, 5, 4, 14]
        self.rotated_L = [self.L, L_90, L_180, L_270]
        J_90 = [15, 5, 4, 3]
        J_180 = [5, 4, 14, 24]
        J_270 = [4, 14, 15, 16]
        self.rotated_J = [self.J, J_90, J_180, J_270]
        self.rotated_O = [self.O]
        T_90 = [4, 13, 14, 15]
        T_180 = [5, 15, 25, 14]
        T_270 = [4, 5, 6, 15]
        self.rotated_T = [self.T, T_90, T_180, T_270]
        self.pieces = [self.rotated_I, self.rotated_S, self.rotated_Z, self.rotated_L, self.rotated_J, self.rotated_O, self.rotated_T]
        for piece in self.pieces:
            for i in range(len(piece)):
                piece[i] = [n + rshift + (self.columns - 10) * int(str(n)[0]) if len(str(n)) > 1 else n + rshift for n in piece[i]]
        if ask_command:
            self.ask_command()
        else:
            pass

    def exit(self):
        pass


Game = Tetris()
