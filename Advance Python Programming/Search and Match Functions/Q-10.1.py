# Write a Python program to search for a word in a string using re.search().

import re

# Sample string
text = "Hello, welcome to the world of Python programming."

# Word to search
word_to_search = "Python"

# Using re.search() to search for the word in the string
match = re.search(r'\b' + word_to_search + r'\b', text)

# Check if a match is found
if match:
    print(f"'{word_to_search}' found in the string.")
else:
    print(f"'{word_to_search}' not found in the string.")
    