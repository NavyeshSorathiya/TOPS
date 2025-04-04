# Write a Python program to create a class and access its properties using an object.

class Person:
    # Constructor to initialize the object with properties
    def __init__(self, name, age):
        self.name = name  # Property for name
        self.age = age    # Property for age
    
    # Method to display person's details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Creating an object of the class Person
person1 = Person("John", 30)

# Accessing properties using the object
print("Accessing properties using the object:")
print(f"Name: {person1.name}")  # Accessing name property
print(f"Age: {person1.age}")    # Accessing age property

# Calling a method of the class
print("\nDisplaying details using a method:")
person1.display_details()  # Calling the method to display details
