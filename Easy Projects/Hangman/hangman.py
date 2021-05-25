import random
print('H A N G M A N')
words = ['python', 'kotlin', 'javascript', 'java']
start = 1
attempts = 8

while attempts > 0:
    if start == 1:
        test = random.choice(words)
        test_list = list(test)
        test_set = set(test_list)
        length = len(test)
        true_guesses = set()
        false_guesses = set()
        ans = input('Type "play" to play the game, "exit" to quit: ')
    if ans == 'exit':
        break
    elif ans != 'play':
        continue
    start = 0
    print()
    dash = 0
    for i in test:
        if i in true_guesses:
            print(i, end='')
        else:
            dash = dash + 1
            print('-', end='')
    if dash == 0:
        print('\nYou guessed the word!')
        print('You survived!\n')
        start = 1
        attempts = 8
        continue
    guess = input('\nInput a letter: ')
    if len(guess) != 1:
        print("You should input a single letter")
        continue
    if guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a lowercase English letter')
        continue
    if guess in test_set:
        if guess in true_guesses:
            print("You've already guessed this letter")
        true_guesses.add(guess)
    else:
        if guess in false_guesses:
            print("You've already guessed this letter")
        else:
            false_guesses.add(guess)
            print("That letter doesn't appear in the word")
            attempts = attempts - 1
    if attempts == 0:
        print('You lost!\n')
        start = 1
        attempts = 8
