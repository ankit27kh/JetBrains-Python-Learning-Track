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

head_tail = [[head1 + ' ' + head2, tail] for head1, head2, tail in zip(total[:-2], total[1:-1], total[2:])]
head_tail_1 = defaultdict(list)
for pair in head_tail:
    head_tail_1[pair[0]].append(pair[1])
counts = [Counter(i) for i in head_tail_1.values()]
head_tail_2 = {key: count.most_common() for key, count in zip(head_tail_1.keys(), counts)}

i = 0
while i < 10:
    while True:
        first_word = choice(list(head_tail_2.keys()))
        check = first_word.split()
        if first_word[0].isupper() and first_word[-1] not in '!.?' and check[0][-1] not in '!.?':
            sentence = first_word.split()
            temp = sentence.copy()
            break
    while True:
        next_ = temp[-2] + ' ' + temp[-1]
        sentence.append(choices([x[0] for x in head_tail_2[next_]], [x[1] for x in head_tail_2[next_]])[0])
        temp = (sentence[-2] + ' ' + sentence[-1]).split()
        if len(sentence) > 4 and sentence[-1][-1] in '!.?':
            break
    print(*sentence)
    i = i + 1
