from nltk.util import ngrams

sentence = "students use computers for learning"

words = sentence.split()

bigrams = list(ngrams(words, 2))

print(bigrams)
