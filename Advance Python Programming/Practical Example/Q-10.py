# Write a Python program to print custom exceptions.

def custom_error(message):
    return f"Custom error occurred: {message}"

def process_data(data):
    if not isinstance(data, list):
        raise ValueError(custom_error("Data must be a list!"))
    print("Data processed successfully.")


def main():
    data = "This is a string, not a list"
    try:
        process_data(data)
    except ValueError as e:
        print(e)

main()