from collections import Counter

transitions = Counter()

for sentence in training_data:
    tags = [tag for word, tag in sentence]

    for i in range(len(tags) - 1):
        pair = (tags[i], tags[i + 1])
        transitions[pair] += 1

print(transitions)
