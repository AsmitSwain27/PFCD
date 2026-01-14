# Question 1
# Write a function that takes a string as a parameter and returns a string with every 
# successive repetitive character replaced with a star(*). For example, 'balloon' is 
# returned as 'bal*o*n'.

def replace_repetitive_chars(s):
    if not s:
        return s
    
    result = [s[0]]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            result.append('*')
        else:
            result.append(s[i])
    
    return ''.join(result)

# Test
test_strings = ['balloon', 'hello', 'Mississippi', 'aabbccdd', 'abc']

for test in test_strings:
    print(f"'{test}' -> '{replace_repetitive_chars(test)}'")
