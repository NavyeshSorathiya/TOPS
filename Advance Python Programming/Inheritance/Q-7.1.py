# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

# Single Inheritance
# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an object of Dog class
dog = Dog()
dog.speak()     # Inherited method from Animal class
dog.bark()      # Method of Dog class

# Multiple Inheritance
# Parent class 1
class Animal:
    def speak(self):
        print("Animal speaks")

# Paren class 2
class Bird:
    def fly(self):
        print("Bird flies")

# Child class inheriting from both Animal and Bird
class Dog(Animal, Bird):
    def bark(self):
        print("Dog barks")

# Creating an object of the child class
dog = Dog()
dog.speak()
dog.fly()
dog.bark()