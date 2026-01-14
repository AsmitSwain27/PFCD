# Question 14
# Write a Python program to reverse the middle half of characters in a string.

def reverse_middle_half(s):
    length = len(s)
    
    if length < 2:
        return s
    
    # Calculate the middle half
    quarter = length // 4
    start = quarter
    end = length - quarter
    
    # Reverse the middle half
    result = s[:start] + s[start:end][::-1] + s[end:]
    
    return result

# Test
test_strings = [
    "abcdefgh",       # 8 chars: reverse middle 4 (cdef)
    "hello",          # 5 chars: reverse middle 2 (ll)
    "python",         # 6 chars: reverse middle 3 (yth)
    "programming",    # 11 chars
    "ab"
]

for test in test_strings:
    result = reverse_middle_half(test)
    print(f"Original: '{test}'")
    print(f"Reversed middle half: '{result}'")
    print()
