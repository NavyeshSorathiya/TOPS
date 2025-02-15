# Write a generator function that generates the first 10 even numbers.


def even_numbers():
    for i in range(1, 11):
        yield i * 2


evens = even_numbers()
print(evens.__next__)
print(list(evens))
