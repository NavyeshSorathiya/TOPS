# Simple Calculator

def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))


    while True:
        print("Press 1 for Addition")
        print("Press 2 for Subtraction")
        print("Press 3 for Multiplication")
        print("Press 4 for Division")
        print("Press 5 to exit")
        choice = int(input("Enter Your choice: "))
        if choice == 1:
            c = a + b
            print(f"Addition of {a} and {b} is: ",c)
        elif choice == 2:
            c = a - b
            print(f"Subtraction of {a} and {b} is: ",c)
        elif choice  == 3:
            c = a * b
            print(f"Multiplication of {a} and {b} is: ",c)
        elif choice == 4:
            c = a / b
            print(f"Division of {a} and {b} is: ",c)
        elif choice == 5:
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Please! Enter valid Number.")

calculator()


def grade():
    stud_id = input("Enter Student ID: ")
    stud_name = input("Enter Student Name: ")
    marks = []
    total = 0
    for i in range(5):
        mark = int(input(f"Enter marks of subject{i + 1}: "))
        marks.append(mark)
        total += mark

    per = total / 5

    if per >= 80:
        grade = "A+"
    elif per >= 70:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 50:
        grade = "C"
    elif per >= 40:
        grade = "D"
    else:
        grade = "Fail"
    
    # Print the result
    print("Student ID | Student Name | S1 | S2 | S3 | S4 | S5 | Total | Percentage | Grade")
    print(f"{stud_id} | {stud_name}  | {marks[0]} | {marks[1]} | {marks[2]} | {marks[3]} | {marks[4]} | {total} | {per} | {grade}")


grade()