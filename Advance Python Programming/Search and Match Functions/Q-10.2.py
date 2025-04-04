# Write a Python program to match a word in a string using re.match().

import re

# Sample string
text = "Hello, welcome to the world of Python programming."

# Word to match
word_to_match = "Hello"

# Using re.match() to check if the word is at the beginning of the string
match = re.match(r'\b' + word_to_match + r'\b', text)

# Check if a match is found
if match:
    print(f"'{word_to_match}' matches at the beginning of the string.")
else:
    print(f"'{word_to_match}' does not match at the beginning of the string.")
