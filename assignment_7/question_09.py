# Question 9
# Create a program to find the number of vowels and consonants in a string.

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Test
test_strings = [
    "Hello World",
    "Python Programming",
    "aeiou",
    "bcdfg",
    "The quick brown fox jumps over the lazy dog"
]

for test in test_strings:
    vowels, consonants = count_vowels_consonants(test)
    print(f"String: '{test}'")
    print(f"Vowels: {vowels}, Consonants: {consonants}")
    print()
