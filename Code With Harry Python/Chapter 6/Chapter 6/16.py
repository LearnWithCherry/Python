# Mini grading system with GPA conversion

marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
else:
    if marks >= 90:
        grade = "A+"
        gpa = 10
    elif marks >= 80:
        grade = "A"
        gpa = 9
    elif marks >= 70:
        grade = "B+"
        gpa = 8
    elif marks >= 60:
        grade = "B"
        gpa = 7
    elif marks >= 50:
        grade = "C"
        gpa = 6
    elif marks >= 40:
        grade = "D"
        gpa = 5
    else:
        grade = "F (Fail)"
        gpa = 0
    
    print(f"Grade: {grade}")
    print(f"GPA: {gpa}")
