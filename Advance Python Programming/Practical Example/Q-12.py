# Write a Python program to demonstrate the use of local and global variables in a class.

global_variable = "I am a global variable"

class MyClass:
    def __init__(self, name):
        self.name = name

    def display(self):
        local_variable = "I am a local variable inside the method"
        print(local_variable)

        print(f"Accessing global variable: {global_variable}")
        print(f"Accessing instance variable (name): {self.name}")

obj = MyClass("Jhon")

obj.display()

print(f"\nAccessing global variable outside the class: {global_variable}")