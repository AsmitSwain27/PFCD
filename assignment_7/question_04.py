# Question 4
# Create a program to count the number of occurrences of a specific character in a string.

def count_character_occurrences(string, char):
    return string.count(char)

# Test
test_string = input("Enter a string: ")
char_to_find = input("Enter the character to count: ")

count = count_character_occurrences(test_string, char_to_find)

print(f"\nString: '{test_string}'")
print(f"Character: '{char_to_find}'")
print(f"Number of occurrences: {count}")
