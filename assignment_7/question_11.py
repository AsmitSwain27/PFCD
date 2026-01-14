# Question 11
# Write a script that reads a line of text, tokenizes the line using space characters 
# as delimiters and outputs only those words beginning with the letter 'b' and ending 
# with the letter 'd'.

def filter_words(text):
    # Tokenize using split
    words = text.split()
    
    # Filter words beginning with 'b' and ending with 'd'
    filtered = [word for word in words if word.lower().startswith('b') and word.lower().endswith('d')]
    
    return filtered

# Test
text = input("Enter a line of text: ")

filtered_words = filter_words(text)

print("\nOriginal text:", text)
print(f"Words beginning with 'b' and ending with 'd': {filtered_words}")
