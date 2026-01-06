# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.


marks_english = int(input("Enter student marks He She got in English : "))
marks_python = int(input("Enter student marks He She got in Python : "))
marks_data_structure = int(input("Enter student marks He She got in DSA : "))
marks_communication = int(input("Enter student marks He She got in Communication : "))

total_percentage = ((marks_english + marks_python + marks_data_structure + marks_communication) / 4)
# print(total_percentage)

if(total_percentage >= 40 ):
    print(f"Student passed with {total_percentage}")
    print(f"Marks in English {marks_english}")
    print(f"Marks in DSA {marks_data_structure}")
    print(f"Marks in python {marks_python}")
    print(f"Marks in communication {marks_communication}")
else:
    print(f"Student couldn't passed the exam \n his/her percentage is {total_percentage}")
    print(f"Marks in English {marks_english}")
    print(f"Marks in DSA {marks_data_structure}")
    print(f"Marks in python {marks_python}")
    print(f"Marks in communication {marks_communication}")