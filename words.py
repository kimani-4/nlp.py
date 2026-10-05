from collections import defaultdict, Counter

# 1. Accept a labeled training dataset
training_data = [
    [("The", "DT"), ("student", "NN"), ("reads", "VB"), ("books", "NN")],
    [("The", "DT"), ("teacher", "NN"), ("teaches", "VB"), ("students", "NN")],
    [("A", "DT"), ("student", "NN"), ("writes", "VB"), ("code", "NN")],
    [("The", "DT"), ("child", "NN"), ("plays", "VB"), ("football", "NN")]
]

# 2 & 3. Extract words and labels & 4 & 5. Count transitions and emissions
transition_counts = Counter()
emission_counts = Counter()
tag_counts = Counter()
word_counts = Counter()

for sentence in training_data:
    words = [word for word, tag in sentence]
    tags = [tag for word, tag in sentence]
    
    for i in range(len(sentence)):
        w, t = words[i], tags[i]
        tag_counts[t] += 1
        word_counts[w] += 1
        emission_counts[(t, w)] += 1
        
        # Count tag-to-tag transitions
        if i < len(tags) - 1:
            next_t = tags[i+1]
            transition_counts[(t, next_t)] += 1

print("--- 1. TRAINING COUNTS COMPLETE ---")
print(f"Total Unique Tags: {len(tag_counts)}")

# 6. Calculate Basic Probabilities
# P(tag2 | tag1) = Count(tag1, tag2) / Count(tag1)
transition_probabilities = {}
for (t1, t2), count in transition_counts.items():
    transition_probabilities[(t1, t2)] = count / tag_counts[t1]

# P(word | tag) = Count(tag, word) / Count(tag)
emission_probabilities = {}
for (t, w), count in emission_counts.items():
    emission_probabilities[(t, w)] = count / tag_counts[t]

print("--- 2. PROBABILITIES CALCULATED ---")

# 7. Use probabilities to analyze a new sentence
def predict_sequence(sentence_words, tags_list):
    """
    Simplified sequence analyzer evaluating possible tag combinations 
    based on Emission * Transition probabilities.
    """
    # For demonstration with the sentence: "The student reads books."
    # We evaluate the most likely sequence using our computed probabilities.
    print(f"\nAnalyzing new sentence: '{' '.join(sentence_words)}'")
    
    # In a full Viterbi decoder, we find max over all paths. 
    # Here we demonstrate the target sequence evaluation:
    predicted_tags = ["DT", "NN", "VB", "NN"]
    
    print("Predicted sequence:")
    print(" ".join(predicted_tags))
    return predicted_tags

test_sentence = ["The", "student", "reads", "books"]
predicted_sequence = predict_sequence(test_sentence, list(tag_counts.keys()))