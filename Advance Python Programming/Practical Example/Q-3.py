# Write a Python program to create a file and write a string into it

datafile = open("datafile.txt", 'w')
datafile.write("Hello, this is a sample string written into the file.")

print(f"String has been written to datafile.txt")