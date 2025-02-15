# Write a Python program that filters out even numbers using the filter() function.
def is_odd(n):
    return n % 2 != 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = filter(is_odd, numbers)

odd_numbers_list = list(odd_numbers)
print("Odd numbers:", odd_numbers_list)