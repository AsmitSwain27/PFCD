# Question 22
# Write a python program to check if a string is symmetric or asymmetric.

def is_symmetric(s):
    # Remove spaces and convert to lowercase for comparison
    s_clean = s.replace(" ", "").lower()
    
    # Check if string is equal to its reverse
    return s_clean == s_clean[::-1]

# Test
test_strings = [
    "madam",
    "racecar",
    "hello",
    "A man a plan a canal Panama",
    "python",
    "noon",
    "level"
]

for test in test_strings:
    result = is_symmetric(test)
    status = "Symmetric (Palindrome)" if result else "Asymmetric"
    print(f"'{test}': {status}")
