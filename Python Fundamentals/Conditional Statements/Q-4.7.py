stud_id = input("Enter student ID: ")
stud_name = input("Enter student Name: ")
s1 = int(input("Enter marks of subject1: "))
s2 = int(input("Enter marks of subject2: "))
s3 = int(input("Enter marks of subject3: "))
s4 = int(input("Enter marks of subject4: "))
s5 = int(input("Enter marks of subject5: "))

tot = s1 + s2 + s3 + s4 + s5
per = tot/5

if per >=80:
    grade = "A+"
    print(grade)
elif per >= 70:
    grade = "A"
    print(grade)
elif per >= 60:
    grade = "B"
    print(grade)
elif per >= 50:
    grade = "C"
    print(grade)
elif per >= 40:
    grade = "D"
    print(grade)
else:
    print("Fail")