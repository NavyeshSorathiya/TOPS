# Write a Python program to update a value in a dictionary


# Update dictionary without using update()
my_dict = {'category':'fruits','name':'tomato','color': 'green'}
my_dict['color'] = 'red'
print(my_dict)

# Update dictionary using update()
dict1 = {'category':'vegetables'}
my_dict.update(dict1)
print(my_dict)