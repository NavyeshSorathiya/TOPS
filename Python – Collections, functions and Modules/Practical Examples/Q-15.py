# Write a Python program to update a value at a particular key in a dictionary.

my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'job': 'Manager',
    'hobby': 'Traveling',
    'country': 'USA'
}

my_dict['job'] = "Engineer"
print(my_dict)

my_dict.update({'age': 25})
print(my_dict)

my_dict.update({'age':30, 'city': 'Los Angeles'})
print(my_dict)

my_dict.setdefault('age', 31)
print(my_dict)