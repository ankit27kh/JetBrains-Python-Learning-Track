import random

n = int(input('Enter the number of friends joining (including you):\n'))
if n > 0:
    names = {}
    print('Enter the name of every friend (including you), each on a new line:')
    while n > 0:
        names[input()] = 0
        n = n - 1
    print('Enter the total bill value:')
    bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    ans = input()
    if ans == 'Yes':
        lucky = random.choice(list(names.keys()))
        print(f'{lucky} is the lucky one!')
        split_bill = round(bill / (len(names) - 1), 2)
        names = {name: split_bill for name in names}
        names[lucky] = 0
        print(names)
    else:
        print('No one is going to be lucky')
        split_bill = round(bill / len(names), 2)
        names = {name: split_bill for name in names}
        print(names)
else:
    print('No one is joining for the party')
