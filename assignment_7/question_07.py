# Question 7
# Write a Python program that checks if a string is a "rotational palindrome." 
# A rotational palindrome is a string that can be rearranged cyclically to form a palindrome.

def is_rotational_palindrome(s):
    # A string can be rearranged to form a palindrome if at most one character
    # has an odd frequency
    from collections import Counter
    
    char_count = Counter(s.lower().replace(" ", ""))
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    return odd_count <= 1

# Test
test_strings = [
    "aab",
    "racecar",
    "hello",
    "civic",
    "aabbcc",
    "abcba",
    "abc"
]

for test in test_strings:
    result = is_rotational_palindrome(test)
    print(f"'{test}' can be rearranged to palindrome: {result}")
