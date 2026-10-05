training_data = [
        [("The", "DT"),
     ("student", "NN"),
     ("reads", "VB")],

    [("The", "DT"),
     ("teacher", "NN"),
     ("teaches", "VB")],

    [("A", "DT"),
     ("student", "NN"),
     ("writes", "VB")]
]
for sentence in training_data:
    words = [word for word, tag in sentence]
    tags = [tag for word, tag in sentence]

    print("Words:", words)
    print("Tags:", tags)
from collections import Counter

transitions = Counter()

for sentence in training_data:
    tags = [tag for word, tag in sentence]

    for i in range(len(tags) - 1):
        pair = (tags[i], tags[i + 1])
        transitions[pair] += 1

print(transitions)
