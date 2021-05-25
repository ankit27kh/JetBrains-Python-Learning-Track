import random


class CalculatorTest:
    ans = 0
    user_ans = 0
    marks = 0
    n_ques = 0
    max_ques = 5

    def __init__(self):
        self.num_a = 0
        self.num_b = 0
        self.operator = ''
        self.level = 0
        self.level_select()
        self.name = ''
        self.level_des = ''

    def level_select(self):
        print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
        try:
            self.level = int(input())
            if self.level == 1:
                self.level_des = 'simple operations with numbers 2-9'
                self.make_ques(self.n_ques, 1)
            elif self.level == 2:
                self.level_des = 'integral squares of 11-29'
                self.make_ques(self.n_ques, 2)
            else:
                print('Incorrect format.')
                self.level_select()
        except Exception:
            print('Incorrect format.')
            self.level_select()

    def make_ques(self, n, level):
        if level == 1:
            if n < self.max_ques:
                self.num_a = random.randint(2, 9)
                self.num_b = random.randint(2, 9)
                self.operator = random.choice(['+', '-', '*'])
                string = f'{self.num_a} {self.operator} {self.num_b}'
                print(string)
                self.n_ques = n + 1
                self.take_input()
            else:
                self.final()
        else:
            if n < self.max_ques:
                self.num_a = random.randint(11, 29)
                print(self.num_a)
                self.n_ques = n + 1
                self.take_input()
            else:
                self.final()

    def take_input(self):
        try:
            self.user_ans = int(input())
            if self.level == 1:
                self.solve(self.num_a, self.num_b, self.operator)
            else:
                self.check(self.num_a ** 2, self.user_ans)
        except Exception:
            print('Incorrect format.')
            self.take_input()

    def solve(self, a, b, op):
        if op == '+':
            self.ans = a + b
        elif op == '-':
            self.ans = a - b
        elif op == '*':
            self.ans = a * b
        self.check(self.ans, self.user_ans)

    def check(self, ans, user):
        if ans == user:
            print('Right!')
            self.marks = self.marks + 1
            self.make_ques(self.n_ques, self.level)
        else:
            print('Wrong!')
            self.make_ques(self.n_ques, self.level)

    def final(self):
        print(f'Your mark is {self.marks}/{self.n_ques}')
        print('Would you like to save your result to the file? Enter yes or no.')
        request = input()
        if request.lower() == 'yes' or request == 'y':
            print('What is your name?')
            self.name = input()
            self.write_file()
        else:
            self.quit()

    def write_file(self):
        with open('results.txt', 'a') as result:
            result.write(f'{self.name}: {self.marks}/{self.max_ques} in level {self.level} ({self.level_des}).')
            print('The results are saved in "results.txt".')
        self.quit()

    def quit(self):
        pass


calc = CalculatorTest()
