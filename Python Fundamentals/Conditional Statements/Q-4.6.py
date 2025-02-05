a = int(input("Enter any numbder: "))
b = a - 1

if a>1:
    if a%b != 0:
        print(f"{a} is a prime number.")
    else:
        print(f"{a} is not a prime number.")
else:
    print(f"{a} is not a prime number.")