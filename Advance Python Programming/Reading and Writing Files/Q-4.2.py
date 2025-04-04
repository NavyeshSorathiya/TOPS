# Write a Python program to write multiple strings into a file.

# Open the file in write mode ('w') or append mode ('a')
datafile = open("datafile.txt", "w")
# Write multiple strings to the file
datafile.write("Hello, this is the first string.\n")
datafile.write("Here comes the second string.\n")
datafile.write("This is the third and final string.\n")

print("Strings have been written to 'datafile.txt'.")