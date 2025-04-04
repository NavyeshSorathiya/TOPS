# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

def divide_number(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e} - You cannot divide by zero!")
        return None

def read_file(filename):
    try:
        number_file = open('number_file', 'r')
        return number_file.read()
    except FileExistsError as e:
        print(f"Error: {e} - The file '{number_file}' was not found!")
        return None
    except IOError as e:
        print(f"Error: {e} - An error occurred while reading the file")
        return None

def main():
    num1 = 10
    num2 = 0
    result = divide_number(num1, num2)
    if result is not None:
        print(f"Result of division: {result}")

    filename = 'none_existen_file.txt'
    file_content = read_file(filename)
    if file_content is not None:
        print("File content:")
        print(file_content)

main()