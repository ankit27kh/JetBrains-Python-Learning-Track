import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
import nltk as nltk
from lxml import etree

# Read the file
root = etree.parse('news.xml').getroot()
news_set = root[0]

# Get headlines and body
headlines = []
texts = []
for news in news_set:
    headlines.append(news[0].text)
    texts.append(news[1].text)

# Tokenize the body
text_tokens = []
for text in texts:
    text_tokens.append(nltk.tokenize.word_tokenize(text.lower()))

# Lemmatize the tokens
better_tokens = []
lemmer = WordNetLemmatizer()
for words in text_tokens:
    better_tokens.append([lemmer.lemmatize(word) for word in words])

# Remove stopwords and punctuation from the tokens
stops = stopwords.words('english')
punc = list(string.punctuation)
best_tokens = []
for text in better_tokens:
    best_tokens.append([word for word in text if (word not in stops) and (word not in punc)])

# Get POS tags for the tokens
pos_tokens = []
for tokens in best_tokens:
    pos_tokens.append([nltk.pos_tag([token])[0] for token in tokens])

# Only work with noun tokens
noun_tokens = []
for pos in pos_tokens:
    noun_tokens.append([x[0] for x in pos if x[1] == 'NN'])

# Make vocabulary list of all nouns
all_nouns = []
for noun_list in noun_tokens:
    all_nouns.extend(noun_list)
vocab = []
for word in all_nouns:
    if word in vocab:
        pass
    else:
        vocab.append(word)

# These are news items with only nouns
noun_only_news = [' '.join(tokens) for tokens in noun_tokens]

# Use Tfidf on noun_only_texts
vectorizer = TfidfVectorizer(vocabulary=vocab)
tfidf_matrix = vectorizer.fit_transform(noun_only_news)
by_max_tfdif = []

# Find words with top scores and clear ties by sorting in reverse descending order
for i in range(10):
    by_max_tfdif.append(tfidf_matrix[i].toarray().argsort()[0, ::-1][:10])
top_words = []
for item, i in zip(by_max_tfdif, range(10)):
    words = [vocab[index] for index in item]
    scores = [tfidf_matrix[i, index] for index in item]
    final = [[word, score] for word, score in zip(words, scores) if word in vocab]
    final.sort(key=lambda x: (x[1], x[0]), reverse=True)
    top_words.append(final)

# Print out the results
# Headlines with 5 top scoring words
for headline, tops in zip(headlines, top_words):
    print(headline + ':')
    i = 1
    for top in tops:
        if i <= 5:
            print(top[0], end=' ')
            i = i + 1
        else:
            break
    print()
    print()
