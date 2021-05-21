import argparse
import math

parser = argparse.ArgumentParser(description='Calculate annuity or differentiated payments and related quantities.')
parser.add_argument('--type', help='diff for differentiated and annuity for annuity')
parser.add_argument('--principal', type=float, help='principal loan amount')
parser.add_argument('--payment', type=float, help='monthly payment')
parser.add_argument('--periods', type=int, help='number of monthly payments')
parser.add_argument('--interest', type=float, help='loan interest rate')

args = parser.parse_args()
method = args.type
P = args.principal
A = args.payment
n = args.periods
interest = args.interest
out = 0
check = [P, A, n]

if check.count(None) > 1 or method is None or interest is None:
    out = 1
if P is not None and P < 0:
    out = 1
if A is not None and A < 0:
    out = 1
if n is not None and n < 0:
    out = 1

if out == 0:
    i = interest / 12 / 100
    if method == 'annuity':
        if n is None:
            n = math.log(A / (A - i * P), 1 + i)
            n = math.ceil(n)
            years = n // 12
            months = n % 12
            if years == 0 and months != 1:
                print(f'It will take {months} months to repay this loan!')
            elif years == 0:
                print(f'It will take {months} month to repay this loan!')
            elif months != 0:
                print(f'It will take {years} years and {months} months to repay this loan!')
            elif years == 1:
                print(f'It will take {years} year to repay this loan!')
            else:
                print(f'It will take {years} years to repay this loan!')

        if A is None:
            A = P * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)
            A = math.ceil(A)
            print(f'Your monthly payment = {A}!')

        if P is None:
            P = A / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
            print(f'Your loan principal = {P}!')

        overpayment = int(A * n - P)
        print(f'Overpayment = {overpayment}')

    if method == 'diff':
        total = 0
        for month in range(1, n + 1):
            D_month = (P / n) + i * (P - (P * (month - 1)) / n)
            D_month = math.ceil(D_month)
            total = total + D_month
            print(f'Month {month}: payment is {D_month}')
        overpayment = int(total - P)
        print(f'Overpayment = {overpayment}')
else:
    print('Incorrect parameters')
