# Question 23
# Given a string s and index i, write a python program to delete the i-th value from s.

def delete_char_at_index(s, i):
    if i < 0 or i >= len(s):
        return "Index out of range"
    
    # Create new string without character at index i
    return s[:i] + s[i+1:]

# Test
test_string = input("Enter a string: ")
index = int(input("Enter the index to delete: "))

result = delete_char_at_index(test_string, index)

print(f"\nOriginal string: '{test_string}'")
print(f"Index to delete: {index}")
print(f"Result: '{result}'")
