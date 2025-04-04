# Write a Python program to open a file in write mode, write some text, and then close it.

datafile = open("datafile.txt", "w")
datafile.write("Hello, this is a sample text written to the file.\n")
datafile.write("Python makes file handling easy!\n")
datafile.close()

print("File written successfully.")