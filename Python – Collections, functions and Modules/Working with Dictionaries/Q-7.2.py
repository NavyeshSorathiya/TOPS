# Write a Python program to merge two lists into one dictionary using a loop

a = ['category','name','color']
b = ['vegetables','chilli','red']

my_dict = {}
for key, value in zip(a, b):
    my_dict[key] = value

print(my_dict)