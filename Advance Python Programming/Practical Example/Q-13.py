# Write a Python program to show single inheritance.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")

    def display_breed(self):
        print(f"{self.name} is a {self.breed} breed")

dog1 = Dog("Buddy", "Golden Retriever")

dog1.speak()
dog1.display_breed()