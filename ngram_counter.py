from collections import Counter
import string
import nltk
from nltk.util import ngrams

# 1. Accept a paragraph (you can replace this with your own text or input())
paragraph = (
    "Students use computers to learn computer science. "
    "Students use computers every single day. "
    "Computer science students use labs to learn programming."
)

# 2. Convert the paragraph to lowercase
paragraph_lower = paragraph.lower()

# 3. Tokenise the paragraph and filter out punctuation marks
tokens = [
    word
    for word in nltk.word_tokenize(paragraph_lower)
    if word not in string.punctuation
]

# 4, 5, 6. Generate unigrams, bigrams, and trigrams
unigrams = list(ngrams(tokens, 1))
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

# Combine all generated N-grams into string formats for frequency analysis
all_ngrams = (
    [" ".join(gram) for gram in unigrams]
    + [" ".join(gram) for gram in bigrams]
    + [" ".join(gram) for gram in trigrams]
)

# 7. Count their frequencies
ngram_counts = Counter(all_ngrams)

# 8. Display the five most frequent N-grams in a table format
print(f"{'N-gram':<25} | {'Frequency'}")
print("-" * 38)
for ngram, freq in ngram_counts.most_common(5):
  print(f"{ngram:<25} | {freq}")