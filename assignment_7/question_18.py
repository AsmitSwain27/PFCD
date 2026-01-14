# Question 18
# What will be the output of executing each of the following statements after assigning 
# the variable: quote = "The quick brown fox jumps over the lazy dog"

print("Question 18: String Method Outputs")
print("="*60)

quote = "The quick brown fox jumps over the lazy dog"
print(f"quote = '{quote}'")
print()

# (a)
print("(a) quote.upper()")
print(f"    Output: '{quote.upper()}'")
print()

# (b)
print("(b) quote[::−1]")
print(f"    Output: '{quote[::-1]}'")
print()

# (c)
print("(c) quote[4:19]")
print(f"    Output: '{quote[4:19]}'")
print()

# (d)
print("(d) quote.replace('fox', 'cat')")
print(f"    Output: '{quote.replace('fox', 'cat')}'")
print()

# (e)
print("(e) quote.count('o')")
print(f"    Output: {quote.count('o')}")
print()

# (f)
print("(f) quote.startswith('The')")
print(f"    Output: {quote.startswith('The')}")
print()

# (g)
print("(g) 'brown' in quote")
print(f"    Output: {'brown' in quote}")
print()

# (h)
print("(h) quote.islower()")
print(f"    Output: {quote.islower()}")
