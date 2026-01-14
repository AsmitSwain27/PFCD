# Question 2
# Write a function that takes two strings and returns True if they are anagrams and 
# False otherwise. A pair of strings is anagram if the letters in one word can be 
# rearranged to form the second one.

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters are equal
    return sorted(str1) == sorted(str2)

# Test
test_pairs = [
    ("listen", "silent"),
    ("hello", "world"),
    ("Dormitory", "Dirty room"),
    ("The eyes", "They see"),
    ("abc", "def")
]

for str1, str2 in test_pairs:
    result = are_anagrams(str1, str2)
    print(f"'{str1}' and '{str2}': {result}")
