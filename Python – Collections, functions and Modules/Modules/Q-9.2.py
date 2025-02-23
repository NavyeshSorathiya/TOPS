# Write a Python program to generate random numbers using the random module

import random

num1 = random.random()
print("Random number is between 0 to 1:",num1)

num2 = random.randint(1, 100)
print("Random number is between 1 to 100: ",num2)

choice_list = random.choice(["Apple", "Banana", "Orange", "Grapes"])
print("Random choice from Choice list:",choice_list)


fruit_list = ["Apple", "Banana", "Orange", "Grapes"]
random.shuffle(fruit_list)
print("Shuffle fruit list : ",fruit_list)