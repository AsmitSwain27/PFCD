# Question 17
# What are the outputs of the below codes and why?

print("Question 17: Output Analysis")
print("="*60)

# (a)
print("\n(a) s = 'how now brown cow'")
print("    print(s[s.find('o'):s.rfind('o')])")
s = "how now brown cow"
result = s[s.find('o'):s.rfind('o')]
print(f"    Output: '{result}'")
print("    Explanation: find('o') finds first 'o' at index 1")
print("                 rfind('o') finds last 'o' at index 16")
print("                 s[1:16] gives 'ow now brown c'")

# (b)
print("\n(b) chr(ord('A') + 2) + chr(ord('Z') - 3)")
result = chr(ord('A') + 2) + chr(ord('Z') - 3)
print(f"    Output: '{result}'")
print("    Explanation: ord('A')=65, chr(67)='C'")
print("                 ord('Z')=90, chr(87)='W'")
print("                 Result: 'CW'")

# (c)
print("\n(c) s = 'abc123def456ghi789'")
print("    indices = [i for i, c in enumerate(s) if c == ']']")
print("    result = s[indices[1]+1:indices[2]] + s[indices[4]+1:]")
print("    print(result)")
s = "abc123def456ghi789"
indices = [i for i, c in enumerate(s) if c == ']']
print(f"    Output: Error! No ']' character found in string")
print(f"    indices list will be empty: {indices}")
print("    Accessing indices[1] will raise IndexError")

# (d)
print("\n(d) s = 'abracadabra'")
print("    print(s.replace(s[s.find('a'):s.rfind('a')], 'XYZ'))")
s = "abracadabra"
result = s.replace(s[s.find('a'):s.rfind('a')], 'XYZ')
print(f"    Output: '{result}'")
print("    Explanation: s[s.find('a'):s.rfind('a')] = s[0:10] = 'abracadabr'")
print("                 Replace 'abracadabr' with 'XYZ' -> 'XYZa'")

# (e)
print("\n(e) s = 'hello'")
print("    shift = 2")
print("    print(''.join(chr((ord(c) - 97 + shift) % 26 + 97) for c in s))")
s = "hello"
shift = 2
result = ''.join(chr((ord(c) - 97 + shift) % 26 + 97) for c in s)
print(f"    Output: '{result}'")
print("    Explanation: Caesar cipher with shift 2")
print("                 h->j, e->g, l->n, l->n, o->q")

# (f)
print("\n(f) s = 'mississippi'")
print("    print(''.join(sorted(set(s))))")
s = "mississippi"
result = ''.join(sorted(set(s)))
print(f"    Output: '{result}'")
print("    Explanation: set(s) = {'m','i','s','p'}")
print("                 sorted and joined = 'imps'")
