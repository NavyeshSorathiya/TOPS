# Write a Python program to show multilevel inheritance.

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

class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

    def display_info(self):
        print(f"{self.name} is a {self.breed} and is {self.age} months old.")

puppy1 = Puppy("Buddy", "Golden Retriever", 6)

puppy1.speak()
puppy1.display_info()