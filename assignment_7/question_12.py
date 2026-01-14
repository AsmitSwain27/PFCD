# Question 12
# Write a script that reads a five-letter word from the user and produces every possible 
# three-letter string that can be derived from the letters of the five-letter words. 
# For example, the three-letter words produced from the word "bathe" include "ate," "bat," 
# "bet," "tab," "hat," "the," and "tea." Challenge: Investigate the functions from the 
# itertools module, then use an appropriate function from that module for this task.

from itertools import permutations

def generate_three_letter_words(word):
    # Generate all 3-letter permutations
    three_letter_perms = [''.join(p) for p in permutations(word, 3)]
    
    # Remove duplicates by converting to set, then back to sorted list
    unique_words = sorted(set(three_letter_perms))
    
    return unique_words

# Test
word = input("Enter a five-letter word: ")

if len(word) != 5:
    print("Please enter exactly a five-letter word!")
else:
    three_letter_words = generate_three_letter_words(word)
    
    print(f"\nThree-letter strings from '{word}':")
    print(f"Total unique combinations: {len(three_letter_words)}")
    print(three_letter_words)
