# Question 10
# Write a script that reads a line of text as a string, tokenizes the string with the 
# split method and outputs the tokens in reverse order. Use space characters as delimiters.

def tokenize_and_reverse(text):
    # Tokenize using split
    tokens = text.split()
    
    # Reverse the tokens
    reversed_tokens = tokens[::-1]
    
    return reversed_tokens

# Test
text = input("Enter a line of text: ")

tokens = tokenize_and_reverse(text)

print("\nOriginal text:", text)
print("Tokens in reverse order:", ' '.join(tokens))
