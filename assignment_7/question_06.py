# Question 6
# Write a Python function that takes a string and returns a new string where every vowel 
# in the input string is replaced by the next vowel in sequence 
# (a → e, e → i, i → o, o → u, u → a).

def replace_vowels_with_next(s):
    vowel_map = {
        'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
        'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
    }
    
    result = []
    for char in s:
        if char in vowel_map:
            result.append(vowel_map[char])
        else:
            result.append(char)
    
    return ''.join(result)

# Test
test_strings = [
    "hello",
    "beautiful",
    "aeiou",
    "Python Programming",
    "Education"
]

for test in test_strings:
    print(f"'{test}' -> '{replace_vowels_with_next(test)}'")
