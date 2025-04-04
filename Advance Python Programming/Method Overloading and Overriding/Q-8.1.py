# Write Python programs to demonstrate method overloading and method overriding.

class Calculator:
    # Method overloading using default arguments
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an object of the Calculator class
calc = Calculator()

# Calling the method with different numbers of arguments
print("Sum of 5 and 3:", calc.add(5, 3))
print("Sum of 5, 3 and 2:", calc.add(5, 3, 2))
print("Sum of 5:", calc.add(5))
