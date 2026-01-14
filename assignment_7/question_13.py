# Question 13
# Check whether a sentence contains more than one space between words. If so, remove 
# the extra spaces and display the corrected sentence. For example, 'Hello    World' 
# should become 'Hello World'.

def remove_extra_spaces(sentence):
    # Split and rejoin to remove extra spaces
    words = sentence.split()
    return ' '.join(words)

# Test
test_sentences = [
    "Hello    World",
    "This  is    a   sentence",
    "Normal sentence",
    "Too     many       spaces",
    "   Leading and trailing   "
]

for sentence in test_sentences:
    corrected = remove_extra_spaces(sentence)
    print(f"Original:  '{sentence}'")
    print(f"Corrected: '{corrected}'")
    print()
