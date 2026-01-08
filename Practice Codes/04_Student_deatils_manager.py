'''💼 Project Challenge: Student Report Card Manager
   Problem Statement:
                    Allow users to add student data (name, roll number, marks). done

                    Use Object-Oriented Programming to manage student details. done

                    Store all records in a file (students.txt) — one record per line. done

                    Allow the user to view all records (read from file). done

                    Use functions to organize your code cleanly.done''' 



    # ask data
class student:
        def __init__(self, name , roll_number, subject, marks):
                self.name = name
                self.roll_number = roll_number
                self.subject = subject
                self.marks = marks

        def __str__(self):
            return (f"Name of the student is {self.name}\n"
                    f"Roll Number of the {self.name} is {self.roll_number}\n"
                    f"Marks of {self.name} in {self.subject} is {self.marks}\n")

def enter_data():
    name = input("Enter student name: ")
    roll_number = int(input("Enter roll number: "))
    subject = input("Enter Subject name: ")
    marks = int(input("Enter marks: "))
    s = student(name , roll_number , subject , marks)
    print("\n" + str(s))
    print("Data stored Sucessfully")
    # store data
    try:
        with open("15_Daily_Questions\\details.txt", "a") as f:
            f.write("-" * 30 + "\n")
            f.write(str(s))
            f.write("-" * 30 + "\n")
    except FileNotFoundError:
        print("Error")
    # view data 
def record():
    try:
        with open("15_Daily_Questions\\details.txt", "r") as f:
            content = f.read()
            print(content if content else "No records found.")
    except FileNotFoundError:
        print("Error")

def ask():
    while True:
        print("--- Welcome to Report Card Manager ---")
        print("Press:\n1 = Enter Student Data\n2 = View Data\n3 = Exit")
        try:
            a = int(input("Enter your choice: "))
            if a == 1:
                enter_data()
            elif a == 2:
                record()
            elif a == 3:
                print("Bye..Bye..")
                break
            else:
                print("Invalid option, try again.")
        except ValueError:
            print("Choose a correct option (1/2/3).")

ask()