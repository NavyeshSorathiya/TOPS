a = int(input("Enter your Age: "))


if a > 18:
    illness = input("You have any illness Yes/No? ")
    if illness == "Yes" or illness == "No" or illness == "yes" or illness == "no":
        if illness == "No" or illness == "no":
            print("You are eligible to donate Blood")
        else:
            print("You are not eligible to donate Blood")
    else:
        print("Please write only Yes/No")
else:
    print("You are not eligible to donate Blood")