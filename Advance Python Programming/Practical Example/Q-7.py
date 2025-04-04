# Write a Python program to handle exceptions in a calculator.

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by Zero!")
    return a / b

def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")

        try:
            choice = input("Enter choice (1/2/3/4/5): ")

            if choice == "5":
                print("Exiting calculator...")
                break
                
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {substract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
            else:
                print("Invalid input. Please choose a valid operation.")
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
calculator()