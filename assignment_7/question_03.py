# Question 3
# Write a function that takes a sentence as an input parameter and displays the number 
# of words in the sentence.

def count_words(sentence):
    # Split the sentence by whitespace and count
    words = sentence.split()
    return len(words)

# Test
test_sentences = [
    "Hello World",
    "This is a simple sentence",
    "Python programming is fun",
    "One",
    "The quick brown fox jumps over the lazy dog"
]

for sentence in test_sentences:
    count = count_words(sentence)
    print(f"Sentence: '{sentence}'")
    print(f"Number of words: {count}")
    print()
