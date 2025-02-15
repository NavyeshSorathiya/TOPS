# Write a Python program to apply the map() function to squqre a list of numbers.

def square(num):
    return num*2

numbers = [1,2,3,4,5]
result = map(square,numbers)
print(list(result))