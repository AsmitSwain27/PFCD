# Question 16
# Write a code to extract unique characters of a string in sorted order.

def extract_unique_sorted_chars(s):
    # Get unique characters using set, then sort
    unique_chars = sorted(set(s))
    return unique_chars

# Test
test_strings = [
    "hello",
    "programming",
    "aabbccdd",
    "Python",
    "Mississippi"
]

for test in test_strings:
    unique = extract_unique_sorted_chars(test)
    print(f"String: '{test}'")
    print(f"Unique characters (sorted): {unique}")
    print(f"As string: '{''.join(unique)}'")
    print()
