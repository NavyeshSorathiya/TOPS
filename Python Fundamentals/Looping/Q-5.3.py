list = ["apple", "orange", "banana", "cherry"]

target_string = "banana"

for i in list:
    if i == target_string:
        print(f"The target string '{target_string}' is found in the list.")
        break
    else:
        print(f"The target string '{target_string}' is not found in the list.")
        break

