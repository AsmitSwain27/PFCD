# Question 21
# For string1 = 'Python Programming Language', find the corresponding outputs.

import re

print("Question 21: Regular Expression Outputs")
print("="*60)

string1 = 'Python Programming Language'
print(f"string1 = '{string1}'")
print()

# (a)
print("(a) match1 = re.fullmatch(r'[A-Za-z]*', string1)")
print("    print(match1.groups())")
match1 = re.fullmatch(r'[A-Za-z]*', string1)
if match1:
    print(f"    Output: {match1.groups()}")
else:
    print("    Output: None (no match - string contains spaces)")
    print("    Explanation: Pattern expects only letters, but string has spaces")
print()

# (b)
print("(b) match2 = re.sub(r'Programming', 'Coding', string1)")
print("    print(match2)")
match2 = re.sub(r'Programming', 'Coding', string1)
print(f"    Output: '{match2}'")
print("    Explanation: Replaces 'Programming' with 'Coding'")
print()

# (c)
print("(c) match3 = re.split(r'\\s+', string1)")
print("    print(match3)")
match3 = re.split(r'\s+', string1)
print(f"    Output: {match3}")
print("    Explanation: Splits by one or more whitespace characters")
print()

# (d)
print("(d) match8 = re.findall(r'\\w+', string1)")
print("    print(match8)")
match8 = re.findall(r'\w+', string1)
print(f"    Output: {match8}")
print("    Explanation: Finds all word characters (letters/digits/underscore)")
