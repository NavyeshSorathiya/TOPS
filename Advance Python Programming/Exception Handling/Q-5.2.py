# Write a Python program to demonstrate handling multiple exceptions

def open_file():
    try:
        filename = input("Enter the filename to open: ")  # Corrected the assignment here
        datafile = open(filename, 'r')  # Open the file manually
        print(datafile.read())  # Read and print the content of the file
        datafile.close()  # Close the file after reading
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Divide Numbers")
        print("2. Open file")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            divide_numbers()
        elif choice == '2':
            open_file()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
        
main()