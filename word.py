import nltk

sentence = "The student writes a computer program."

words = nltk.word_tokenize(sentence)

tags = nltk.pos_tag(words)
print(tags)