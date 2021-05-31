class MatrixProcessor:

    def __init__(self):
        self.menu()

    def menu(self):
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
        n = input('Your choice: ')
        if n in ['1', '2', '3', '4', '5', '6', '0']:
            if n == '1':
                self.add()
            elif n == '2':
                self.const_multi()
            elif n == '3':
                self.mat_multi()
            elif n == '4':
                self.transpose()
            elif n == '5':
                self.determinant()
            elif n == '6':
                self.inverse()
            elif n == '0':
                self.exit()
        else:
            print('Invalid choice')
            self.menu()

    def add(self):
        A = input('Enter size of first matrix: ').split()
        rowsA = []
        print('Enter first matrix:')
        for i in range(int(A[0])):
            rowsA.append(input().split())
        B = input('Enter size of second matrix: ').split()
        rowsB = []
        print('Enter second matrix:')
        for i in range(int(B[0])):
            rowsB.append(input().split())
        if A != B:
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            ans = []
            for x in range(int(A[0])):
                ans.append([float(i) + float(j) for i, j in zip(rowsA[x], rowsB[x])])
            for i in ans:
                for j in i:
                    print(j, end=' ')
                print()
        print()
        self.menu()

    def const_multi(self):
        A = input('Enter size of matrix: ').split()
        rowsA = []
        print('Enter matrix:')
        for i in range(int(A[0])):
            rowsA.append(input().split())
        c = float(input())
        print('The result is:')
        for i in rowsA:
            for j in i:
                print(float(j) * c, end=' ')
            print()
        print()
        self.menu()

    def mat_multi(self):
        A = input('Enter size of first matrix: ').split()
        rowsA = []
        print('Enter first matrix:')
        for i in range(int(A[0])):
            rowsA.append(input().split())
        B = input('Enter size of second matrix: ').split()
        rowsB = []
        print('Enter second matrix:')
        for i in range(int(B[0])):
            rowsB.append(input().split())
        if A[1] == B[0]:
            ans = []
            for i in range(int(A[0])):
                row = []
                for k in range(int(B[1])):
                    row1 = []
                    for j in range(int(A[1])):
                        row1.append([float(rowsA[i][j]) * float(rowsB[j][k])])
                    row.append(sum([sum(i) for i in row1]))
                ans.append(row)
            print('The result is:')
            for i in ans:
                for j in i:
                    print(float(j), end=' ')
                print()
            print()
        else:
            print('The operation cannot be performed.')
        self.menu()

    def transpose(self):
        print()
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        n = input()
        if n in ['1', '2', '3', '4']:
            A = input('Enter matrix size: ').split()
            rowsA = []
            print('Enter matrix:')
            for i in range(int(A[0])):
                rowsA.append(input().split())
            print('The result is:')
            if n == '1':
                for i in range(int(A[1])):
                    for j in range(int(A[0])):
                        print(rowsA[j][i], end=' ')
                    print()
            elif n == '2':
                for i in range(int(A[1]) - 1, -1, -1):
                    for j in range(int(A[0]) - 1, -1, -1):
                        print(rowsA[j][i], end=' ')
                    print()
            elif n == '3':
                for i in range(int(A[0])):
                    for j in range(int(A[1]) - 1, -1, -1):
                        print(rowsA[i][j], end=' ')
                    print()
            else:
                for i in range(int(A[0]) - 1, -1, -1):
                    for j in range(int(A[1])):
                        print(rowsA[i][j], end=' ')
                    print()
        else:
            print('Invalid choice')
            self.menu()

    def determinant(self):
        A = input('Enter matrix size: ').split()
        if A[0] != A[1]:
            print('Invalid input')
            self.menu()
        else:
            rowsA = []
            print('Enter matrix:')
            for i in range(int(A[0])):
                rowsA.append(input().split())
            print('The result is:')
            print(self.solve_det(rowsA))

    def solve_det(self, matrix):
        if len(matrix) == 1:
            return float(matrix[0][0])
        if len(matrix) == 2:
            return float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
        else:
            i = 1
            total = 0
            temp = matrix[1:]
            for t in range(len(matrix)):
                new = []
                for q in range(len(temp)):
                    new.append(temp[q][0:t] + temp[q][t+1:])
                total = total + ((-1) ** (i + t + 1)) * float(matrix[i - 1][t]) * self.solve_det(new)
            return total

    def inverse(self):
        A = input('Enter matrix size: ').split()
        if A[0] != A[1]:
            print('Invalid input')
            self.menu()
        else:
            rowsA = []
            print('Enter matrix:')
            for i in range(int(A[0])):
                rowsA.append(input().split())
            det = self.solve_det(rowsA)
            if det == 0:
                print("This matrix doesn't have an inverse.")
                print()
                self.menu()
            else:
                cofactor_matrix = []
                for i in range(len(rowsA)):
                    temp = rowsA.copy()
                    temp.pop(i)
                    for t in range(len(rowsA)):
                        new = []
                        for q in range(len(temp)):
                            new.append(temp[q][0:t] + temp[q][t + 1:])
                        cofactor_matrix.append(((-1) ** (i + 1 + t + 1)) * self.solve_det(new))
                co_matrix = []
                for i in range(len(rowsA)):
                    co_matrix.append(cofactor_matrix[i*(len(rowsA)):(i+1)*len(rowsA)])
                new = []
                for i in range(len(co_matrix)):
                    for j in range(len(co_matrix)):
                        new.append(co_matrix[j][i])
                new1 = []
                for i in range(len(rowsA)):
                    new1.append(new[i*(len(rowsA)):(i+1)*len(rowsA)])
                for i in new1:
                    for j in i:
                        print(float(j) / det, end=' ')
                    print()
                print()
                self.menu()

    def exit(self):
        pass


mat = MatrixProcessor()
