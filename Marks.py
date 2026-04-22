name = input("Enter student name:  ")
marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2:  "))
marks3 = int(input("Enter marks 3:  "))
average = (marks1 + marks2 + marks3) / 3

if average >= 50:
    print(f"{name} - Pass!")
else:
    print(f"{name} - Fail!")
print(f"Average marks: {average:.2f}")