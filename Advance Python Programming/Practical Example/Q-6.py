#  6) Write a Python program to check the current position of the file cursor using tell().

file_name = "datafile.txt"

try:
    datafile = open(file_name, 'r')
    datafile.read(10)

    current_position = file.tell()

    print(f"The current position of the file cursor is: {current_position}")

except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except IOError:
    print(f"Error reading the file {file_name}.")

