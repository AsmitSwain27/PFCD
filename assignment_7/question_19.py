# Question 19
# Examine the following string: quote = 'Knowledge is power. Power is gained through knowledge.'
# What will be the output for the following function calls:

print("Question 19: String Method Outputs")
print("="*60)

quote = 'Knowledge is power. Power is gained through knowledge.'
print(f"quote = '{quote}'")
print()

# (a)
print("(a) quote.find('power')")
result = quote.find('power')
print(f"    Output: {result}")
print(f"    Explanation: First occurrence of 'power' at index {result}")
print()

# (b)
print("(b) quote.rfind('knowledge')")
result = quote.rfind('knowledge')
print(f"    Output: {result}")
print(f"    Explanation: Last occurrence of 'knowledge' at index {result}")
print()

# (c)
print("(c) quote.title()")
result = quote.title()
print(f"    Output: '{result}'")
print()

# (d)
print("(d) quote.lower()")
result = quote.lower()
print(f"    Output: '{result}'")
print()

# (e)
print("(e) quote.upper()")
result = quote.upper()
print(f"    Output: '{result}'")
print()

# (f)
print("(f) quote.endswith('knowledge.')")
result = quote.endswith('knowledge.')
print(f"    Output: {result}")
print()

# (g)
print("(g) quote.split(' ')")
result = quote.split(' ')
print(f"    Output: {result}")
print()

# (h)
print("(h) quote.partition('is')")
result = quote.partition('is')
print(f"    Output: {result}")
print(f"    Explanation: Returns tuple (before, separator, after)")
print()

# (i)
print("(i) quote.isalpha()")
result = quote.isalpha()
print(f"    Output: {result}")
print(f"    Explanation: Contains spaces and punctuation, not all alphabetic")
