# Write a Python program to create a parameterized function that takes two arguments and prints their sum.

def sum(a, b):
    return a + b


a = int(input("Enter No.1: "))
b = int(input("Enter No.2: "))
c = sum(a, b)
print(f"Sum of {a} and {b} is",c)