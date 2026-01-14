# Question 25
# Use regular expressions and the findall function to count the number of digits, 
# non-digit characters, whitespace characters and non-whitespace characters in a string.

import re

def count_character_types(s):
    # Count digits
    digits = re.findall(r'\d', s)
    digit_count = len(digits)
    
    # Count non-digit characters
    non_digits = re.findall(r'\D', s)
    non_digit_count = len(non_digits)
    
    # Count whitespace characters
    whitespace = re.findall(r'\s', s)
    whitespace_count = len(whitespace)
    
    # Count non-whitespace characters
    non_whitespace = re.findall(r'\S', s)
    non_whitespace_count = len(non_whitespace)
    
    return {
        'digits': digit_count,
        'non_digits': non_digit_count,
        'whitespace': whitespace_count,
        'non_whitespace': non_whitespace_count,
        'total': len(s)
    }

# Test
test_strings = [
    "Hello World 123",
    "Python 3.11 Programming!",
    "abc 123 xyz 789",
    "NoSpacesHere123",
    "12345"
]

print("Character Type Counting using Regular Expressions")
print("="*60)

for test in test_strings:
    print(f"\nString: '{test}'")
    counts = count_character_types(test)
    print(f"  Digits: {counts['digits']}")
    print(f"  Non-digits: {counts['non_digits']}")
    print(f"  Whitespace: {counts['whitespace']}")
    print(f"  Non-whitespace: {counts['non_whitespace']}")
    print(f"  Total characters: {counts['total']}")
