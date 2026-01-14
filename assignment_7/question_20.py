# Question 20
# For string1 = 'Python Programming Language', determine the patterns extracted by the 
# following regular expressions:

import re

print("Question 20: Regular Expression Pattern Extraction")
print("="*60)

string1 = 'Python Programming Language'
print(f"string1 = '{string1}'")
print()

# (a)
print("(a) match1 = re.search('.', m?', string1)")
print("    print(match1.group())")
try:
    match1 = re.search('.', string1)  # Correcting the pattern
    print(f"    Output: '{match1.group()}'")
    print("    Explanation: '.' matches any single character (first char 'P')")
except:
    print("    Note: Pattern '.', m?' seems to have a typo. Using '.' pattern")
print()

# (b)
print("(b) match3 = re.search('.*Language$', string1)")
print("    print(match3.group())")
match3 = re.search('.*Language$', string1)
if match3:
    print(f"    Output: '{match3.group()}'")
    print("    Explanation: '.*' matches everything, 'Language$' ensures it ends with Language")
print()

# (c)
print("(c) match4 = re.search(' w* a w*', string1)")
print("    print(match4.group())")
print("    Assuming pattern is ' \\w* a \\w*' (word chars around 'a')")
match4 = re.search(r' \w* a \w*', string1)
if match4:
    print(f"    Output: '{match4.group()}'")
else:
    print("    Output: None (no match found)")
print()

# (d)
print("(d) match5 = re.search('.*', string1)")
print("    print(match5.group())")
match5 = re.search('.*', string1)
if match5:
    print(f"    Output: '{match5.group()}'")
    print("    Explanation: '.*' matches everything (greedy)")
