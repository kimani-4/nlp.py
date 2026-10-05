from collections import Counter, defaultdict
import string
import nltk
from nltk.util import ngrams

# --- 1. NEW UNIVERSITY DATASET TEXT ---
dataset_text = """
Lecturers deliver computer science notes. 
Students borrow library books. 
Lecturers grade programming exams.
"""


def analyze_university_text(text):
  print("--- DATASET TEXT ---")
  print(text.strip())
  print("-" * 50)

  # --- 2. CLEANING AND TOKENIZATION ---
  text_lower = text.lower()
  tokens = [
      word
      for word in nltk.word_tokenize(text_lower)
      if word not in string.punctuation
  ]

  print(f"Total Tokens: {len(tokens)}")
  print("-" * 50)

  # --- 3. GENERATE N-GRAMS ---
  unigrams = list(ngrams(tokens, 1))
  bigrams = list(ngrams(tokens, 2))
  trigrams = list(ngrams(tokens, 3))

  uni_strings = [" ".join(g) for g in unigrams]
  bi_strings = [" ".join(g) for g in bigrams]
  tri_strings = [" ".join(g) for g in trigrams]

  # --- 4 & 5. FREQUENCIES & MOST FREQUENT N-GRAMS ---
  print("TOP UNIGRAMS:")
  for gram, freq in Counter(uni_strings).most_common(3):
    print(f"  {gram}: {freq}")

  print("\nTOP BIGRAMS:")
  for gram, freq in Counter(bi_strings).most_common(3):
    print(f"  {gram}: {freq}")

  print("\nTOP TRIGRAMS:")
  for gram, freq in Counter(tri_strings).most_common(3):
    print(f"  {gram}: {freq}")
  print("-" * 50)

  # --- 6 & 7. INTERACTIVE PHRASE LOOKUP (Next Word Prediction) ---
  model = defaultdict(list)
  for w1, w2 in bigrams:
    model[w1].append(w2)

  user_input = (
      input(
          "\nEnter a single word to see what commonly follows it (e.g.,"
          " 'lecturers'): "
      )
      .strip()
      .lower()
  )
  if user_input in model:
    following_counts = Counter(model[user_input])
    print(
        f"Words commonly following '{user_input}':"
        f" {following_counts.most_common(3)}"
    )
  else:
    print(f"'{user_input}' not found in the bigram model dictionary.")

  print("-" * 50)

  # --- 8. POS TAGGING TO SELECTED SENTENCES ---
  sample_sentence = "Lecturers deliver computer science notes."
  sentence_tokens = nltk.word_tokenize(sample_sentence)
  pos_tags = nltk.pos_tag(sentence_tokens)

  print("POS TAGGING RESULTS FOR SAMPLE SENTENCE:")
  print(f"Sentence: '{sample_sentence}'")
  for word, tag in pos_tags:
    print(f"  {word} -> {tag}")


if __name__ == "__main__":
  analyze_university_text(dataset_text)