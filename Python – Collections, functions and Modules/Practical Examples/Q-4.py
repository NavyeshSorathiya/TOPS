# Write a Python program to remove elements from a list using pop() and remove().

a = ["Apple", "Grapes", "Banana", "Orange"]
a.remove("Apple")
print(a)

b = ["Apple", "Banana", "Grapes", "Watermelon", "Mango"]
b.pop()
print(b)        # Remove last element from list

c = ["Banana", "Kiwi", "Pineapple", "Boysenberry"]
c.pop(2)
print(c)        # Remove element fron given specify element
