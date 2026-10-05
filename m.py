from collections import Counter
from nltk.util import ngrams

text = """
students use computers
students use software
students learn programming
"""

words = text.lower().split()

bigrams = list(ngrams(words, 2))

bigram_counts = Counter(bigrams)

print(bigram_counts)
