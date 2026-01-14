# Question 15
# Write a Python program to print the substrings of a character having a particular 
# frequency. For 'aabbbbccccdddd', you should print 'bbb' if particular frequency is 3.

def print_substrings_with_frequency(s, frequency):
    from collections import Counter
    
    # Count character frequencies
    char_count = Counter(s)
    
    # Find characters with the specified frequency
    chars_with_freq = [char for char, count in char_count.items() if count == frequency]
    
    if not chars_with_freq:
        print(f"No characters with frequency {frequency} found.")
        return
    
    print(f"Characters with frequency {frequency}:")
    for char in chars_with_freq:
        substring = char * frequency
        print(f"'{char}' appears {frequency} times: '{substring}'")

# Test
test_string = "aabbbbccccdddd"
print(f"String: '{test_string}'")
print()

# Test with different frequencies
for freq in [2, 3, 4]:
    print(f"\nFrequency {freq}:")
    print_substrings_with_frequency(test_string, freq)
