This is the first project in the 'Hard' category that I completed.

Objectives:

1. Make a list of trigrams. It should consist of heads and tails, heads should consist of two space-separated tokens concatenated into a single string.  
The tails should consist of one token. For example: head — 'winter is', tail — 'coming'.

2. The Markov model should be trained based on the list of trigrams.

3. The beginning of the chain should be a randomly chosen head from the model.

4. When predicting the next word, the model should be fed the concatenation of the last two tokens of the chain separated by a space.

5. Print 10 pseudo-sentences of length 5 of more. Taking care that they start with capitalized words and end with sentence stop symbols- '.!?'.