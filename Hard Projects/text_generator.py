import nltk
from collections import defaultdict, Counter
from random import choice, choices

total = []
file = 'corpus.txt'
# file = input()
with open(file, "r", encoding="utf-8") as f:
    texts = f.readlines()
    for text in texts:
        total.extend(nltk.tokenize.WhitespaceTokenizer().tokenize(text))

unique_total = list(set(total))

"""
print('Corpus statistics:')
print(f'All tokens: {len(total)}')
print(f'Unique tokens: {len(unique_total)}')
print()

while True:
    command = input()
    if command == 'exit':
        break
    try:
        command = int(command)
        if -len(total) < command < len(total) - 1:
            print(total[command])
        else:
            print('Index Error. Please input an integer that is in the range of the corpus.')
    except ValueError:
        print('Type Error. Please input an integer.')
"""

head_tail = [[head1 + ' ' + head2, tail] for head1, head2, tail in zip(total[:-2], total[1:-1], total[2:])]

"""
print(f'Number of bigrams: {len(head_tail)}')
print()
while True:
    command = input()
    if command == 'exit':
        break
    try:
        command = int(command)
        if -len(head_tail) < command < len(head_tail) - 1:
            print(f'Head: {head_tail[command][0]}        Tail: {head_tail[command][1]}')
        else:
            print('Index Error. Please input an integer that is in the range of the corpus.')
    except ValueError:
        print('Type Error. Please input an integer.')
"""

head_tail_1 = defaultdict(list)
for pair in head_tail:
    head_tail_1[pair[0]].append(pair[1])
counts = [Counter(i) for i in head_tail_1.values()]
head_tail_2 = {key: count.most_common() for key, count in zip(head_tail_1.keys(), counts)}

"""
while True:
    command = input()
    if command == 'exit':
        break
    try:
        list_ = head_tail_2[command]
        print(f'Head: {command}')
        for pair in list_:
            print(f'Tail: {pair[0]}\tCount: {pair[1]}')
        print()
    except KeyError:
        print(f'Head: {command}')
        print('Key Error. The requested word is not in the model. Please input another word.')
        print()
"""

i = 0
while i < 10:
    while True:
        first_word = choice(list(head_tail_2.keys()))
        check = first_word.split()
        if first_word[0].isupper() and first_word[-1] not in '!.?' and check[0][-1] not in '!.?':
            sentence = first_word.split()
            temp = sentence.copy()
            # temp = sentence[-1].split()
            break
    while True:
        next_ = temp[-2] + ' ' + temp[-1]
        sentence.append(choices([x[0] for x in head_tail_2[next_]], [x[1] for x in head_tail_2[next_]])[0])
        temp = (sentence[-2] + ' ' + sentence[-1]).split()
        if len(sentence) > 4 and sentence[-1][-1] in '!.?':
            break
    print(*sentence)
    i = i + 1
