# Write a Python program to read the contents of a file and print them on the console.

datafile = open("datafile.txt", "r")
print(datafile.read())
datafile.close()
