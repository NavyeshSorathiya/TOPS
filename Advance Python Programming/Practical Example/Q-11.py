# Write a Python program to create a class and access the properties  of the class using an object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

person1 = Person("John", 25)

print("Accessing properties using object:")
print(f"Person's Name: {person1.name}")
print(f"Person's Age: {person1.age}")

print("\nDisplaying information using method:")
person1.display_info()