# Write a Python program to read a file and print the data on the console.

# Open the file in read mode
file_name = "datafile.txt"

try:
    datafile = open(file_name, 'r')
    datafile.read()
    print(file_name)
except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except IOError:
    print(f"Error reading the file {file_name}.")