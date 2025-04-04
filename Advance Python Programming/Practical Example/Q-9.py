#  Write a Python program to handle file exceptions and use the finally block for closing the file.

def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError as e:
        print(f"Error: {e} - The file '{filename}' was not found!")
    except IOError as e:
        print(f"Error: {e} - An error occurred while reading the file!")
    finally:
        try:
            file.read()
            print("File closed successfully.")
        except NameError:
            print("No file was opened, so nothing to close.")

def main():
    filename = "numbers_file.txt"
    read_file(filename)

main()