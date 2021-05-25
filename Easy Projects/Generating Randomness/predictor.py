length = 100
capital = 1000
print('Please give AI some data to learn...')
print('The current data length is 0, 100 symbols left')


def check_input(new, string):
    for i in new:
        if i in ['0', '1']:
            string = string + i
    if string != '':
        return string
    else:
        return 'some wrong input'


string = ''
while len(string) < 100:
    new = input('Print a random string containing 0 or 1:\n\n')
    string = check_input(new, string)
    if len(string) < 100:
        print(f'Current data length is {len(string)}, {100 - len(string)} symbols left')

print('Final data string:')
print(string)
print()
print('''You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!''')
triads = ['000', '001', '010', '011', '100', '101', '110', '111']


def make_prob(string):
    def find_next(triad, string):
        c0, c1 = 0, 0
        for i in range(len(string) - 3):
            if string[i:i+4] == triad + '0':
                c0 = c0 + 1
            elif string[i:i+4] == triad + '1':
                c1 = c1 + 1
        return c0, c1
    probability_0 = {}
    for tri in triads:
        c0, c1 = find_next(tri, string)
        if c0 > c1:
            probability_0[tri] = 1
        else:
            probability_0[tri] = 0
    return probability_0


probability_0 = make_prob(string)


def prediction(probability_0, new):
    temp = '000'
    for i in range(len(new) - 3):
        test = new[i:i + 3]
        if probability_0[test] == 1:
            temp = temp + '0'
        else:
            temp = temp + '1'
    return temp


while True:
    print()
    new_string = input('Print a random string containing 0 or 1:\n')
    if new_string == 'enough':
        break
    new_string = check_input(new_string, '')
    if new_string == 'some wrong input':
        continue
    print('prediction:')
    predicted_string = prediction(probability_0, new_string)
    print(predicted_string)
    count = 0
    for i in range(len(new_string) - 3):
        if new_string[i + 3] == predicted_string[i + 3]:
            count = count + 1
    print()
    acc = count / (len(new_string) - 3)
    acc = round(acc * 100, 2)
    print(f'Computer guessed right {count} out of {len(new_string) - 3} symbols ({acc} %)')
    capital = capital - count + (len(new_string) - 3 - count)
    print(f'Your capital is now ${capital}')
    string = string + new_string
    probability_0 = make_prob(string)

print('Game over!')
