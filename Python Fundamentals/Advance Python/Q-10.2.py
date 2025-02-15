# Write a Python program that uses reduce() to find the product of a list of numbers
def reduce(func, seq):
    result = seq[0]
    for item in seq[1:]:
        result = func(result, item)
    return result

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]

product = reduce(multiply, numbers)

print("The product of the numbers is:", product)