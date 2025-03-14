# Write a Python program to convert two lists into one dictionary using a for loop.

keys = ['name', 'age', 'city', 'job']
values = ['Alice', '30', 'New York', 'Manager']

res = {}

for keys, values in zip(keys, values):
    res[keys] = values

print(res)