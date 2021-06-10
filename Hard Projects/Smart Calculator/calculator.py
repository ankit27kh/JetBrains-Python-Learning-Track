import string
import sys


class Calculator:

    def __init__(self):
        self.variables = {}
        self.answer = None
        self.take_input()

    def take_input(self):
        while True:
            if self.answer is not None:
                print(self.answer)
                self.answer = None
            initial = input()
            if initial == '':
                self.take_input()
            if initial[0] == '/':
                if initial == '/help':
                    print("""This is a calculator. You can use '+-*/^()' in your expressions.
You can also assign values to variables. Variable names can only contain Latin alphabet.
Type /exit to exit.""")
                    self.take_input()
                elif initial == '/exit':
                    self.exit()
                else:
                    print('Unknown command')
                    self.take_input()
            else:
                self.process_input(initial)

    def exit(self):
        print('Bye!')
        sys.exit()

    def process_input(self, initial):
        equation = []
        breaks = '+-*/()^='
        temp = ''
        for i in initial:
            if i in breaks:
                equation.append(temp)
                equation.append(i)
                temp = ''
            else:
                temp = temp + i
        equation.append(temp)
        equation = [i.strip() for i in equation]
        equation = [i for i in equation if i]
        start = True
        sym_sub = 0
        infix = []
        if equation[-1] in '+-*/(^':
            print('Invalid expression')
            self.take_input()
        for i, j in enumerate(equation):
            if j == '+' and start:
                start = False
            elif j == '+' and equation[i-1] == '+':
                pass
            elif j == '-' and start:
                sym_sub = sym_sub + 1
                start = False
            elif j == '-' and equation[i-1] == '-':
                sym_sub = sym_sub + 1
            elif j.isalnum() and start:
                infix.append(j)
                start = True
            elif j.isalnum() and equation[i-1] == '+':
                infix.append('+')
                infix.append(j)
                start = True
            elif (j.isalnum() or j == '(') and equation[i-1] == '-':
                if sym_sub % 2 == 0:
                    infix.append('+')
                    infix.append(j)
                else:
                    infix.append('-')
                    infix.append(j)
                sym_sub = 0
                start = True
            elif j in '*/^=' and equation[i-1] in '*/=^':
                print('Invalid expression')
                self.take_input()
            elif (j == '+' and equation[i-1] == '-') or (j == '-' and equation[i-1] == '+'):
                print('Invalid expression')
                self.take_input()
            elif j in '*/^=':
                infix.append(j)
                start = True
            elif j == '(' and not equation[i-1].isalnum():
                infix.append(j)
                start = True
            elif j == ')' and equation[i-1].isalnum():
                infix.append(j)
                start = True
            else:
                self.take_input()

        if infix.count('(') == infix.count(')'):
            if '=' in infix:
                self.variable_assignment(infix)
            else:
                self.infix_to_postfix(infix)
        else:
            print('Invalid expression')
            self.take_input()

    def infix_to_postfix(self, infix):
        postfix = []
        operators = []
        breaks = '+-*/^'
        precedence = {'+': '', '-': '', '*': '+-', '/': '+-', '^': '+-*/'}
        first_bra = True
        for i in infix:
            if i.isalnum():
                postfix.append(i)
            elif i in breaks and (operators == [] or operators[-1] == '('):
                operators.append(i)
            elif i in breaks and operators[-1] in precedence[i]:
                operators.append(i)
            elif i in breaks and operators[-1] not in precedence[i]:
                for j in range(len(operators)):
                    if operators[-1] in precedence[i] or operators[-1] == '(':
                        break
                    else:
                        postfix.append(operators.pop())
                operators.append(i)
            elif i == '(':
                operators.append(i)
                first_bra = False
            elif i == ')':
                if first_bra:
                    print('Invalid expression')
                    self.take_input()
                for j in range(len(operators)):
                    if operators[-1] == '(':
                        break
                    else:
                        postfix.append(operators.pop())
                operators.append(i)
                operators.pop()
                operators.pop()

        for j in range(len(operators)):
            op = operators.pop()
            if op in breaks:
                postfix.append(op)
            elif op in ['(', ')']:
                print('Invalid expression')
                self.take_input()
        self.postfix_to_value(postfix)

    def postfix_to_value(self, postfix):
        value = []
        for i in postfix:
            if i.isdigit():
                value.append(i)
            elif i.isalpha():
                result = self.variables.get(i, None)
                if result is None:
                    print('Unknown variable')
                    self.take_input()
                else:
                    value.append(result)
            elif i in '+-*/^':
                a = int(value.pop())
                b = int(value.pop())
                if i == '+':
                    result = b + a
                elif i == '-':
                    result = b - a
                elif i == '*':
                    result = b * a
                elif i == '/':
                    result = b // a
                elif i == '^':
                    result = b ** a
                value.append(result)
        self.answer = value[-1]

    def variable_assignment(self, infix):
        if not self.identifier_check(infix[0]):
            print('Invalid identifier')
            self.take_input()
        elif infix.count('=') > 1:
            print('Invalid identifier')
            self.take_input()
        else:
            for i in infix[2:1]:
                if not self.identifier_check(i):
                    print('Invalid assignment')
                    self.take_input()
            self.infix_to_postfix(infix[2:])
            self.variables[infix[0]] = self.answer
            self.answer = None
            self.take_input()

    def identifier_check(self, variable):
        if any([True for j in variable if j in string.digits]) and any([True for j in variable if j in string.ascii_letters]):
            return False
        else:
            return True


calc = Calculator()
