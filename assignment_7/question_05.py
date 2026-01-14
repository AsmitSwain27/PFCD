# Question 5
# Write a Python program to find the length of the longest word in a sentence.

def find_longest_word_length(sentence):
    words = sentence.split()
    if not words:
        return 0
    
    longest_length = max(len(word) for word in words)
    longest_word = max(words, key=len)
    
    return longest_length, longest_word

# Test
test_sentences = [
    "Python programming is interesting",
    "The quick brown fox",
    "Hello World",
    "Supercalifragilisticexpialidocious is a long word"
]

for sentence in test_sentences:
    length, word = find_longest_word_length(sentence)
    print(f"Sentence: '{sentence}'")
    print(f"Longest word: '{word}' (length: {length})")
    print()
