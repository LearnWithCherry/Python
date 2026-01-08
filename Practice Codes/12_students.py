class Student:
    def __init__(self, name, cls, rollNumber, marks, percentage):
        self.name = name
        self.cls = cls
        self.rollNumber = rollNumber
        self.marks = marks
        self.percentage = percentage
        
    def toUser(self):
        return (f"Name of the student is {self.name}\n"
                f"{self.name} is in {self.cls} class and His/her Roll Number is {self.rollNumber}\n"
                f"{self.name} got {self.marks} Marks and His/Her Percentage is {self.percentage}")

    def toFile(self):
        return f"{self.name},{self.cls},{self.rollNumber},{self.marks},{self.percentage}\n"


def addData():
    name = input("Enter Student Name: ")
    Class = input("Enter Class: ")
    rollNumber = int(input("Enter Roll Number: "))
    marks = int(input("Enter Marks: "))
    percentage = float(input("Enter Percentage: "))
    print("-----Student Details successfully entered-----")
    return Student(name, Class, rollNumber, marks, percentage)



def viewAll():
    filename = "15_Daily_Questions\\project_txt_file\\students.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                print("File is Empty...")
            else:
                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) == 5:  # safeguard
                        stud = Student(parts[0], parts[1], parts[2], parts[3], parts[4])
                        print(stud.toUser(), "\n")
    except FileNotFoundError:
        print("No file found...")


def SaveData(data):
    filename = "15_Daily_Questions\\project_txt_file\\students.txt"
    try:
        with open(filename, "a") as file:
            file.write(data)
    except FileNotFoundError:
        print("No file found...")


def removeData(roll_no):
    filename = "15_Daily_Questions\\project_txt_file\\students.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                if not line.strip().split(",")[2] == str(roll_no):  # skip matching roll no
                    file.write(line)

        print(f"Data with Roll Number {roll_no} removed successfully!")

    except FileNotFoundError:
        print("No file found...")


def menu():
    print("-----Welcome-----")
    while True:
        print("-----Select-----\n1 = Add Data\n2 = View All Data\n3 = Remove Data\n4 = Exit")
        userInput = int(input("Enter your choice (1/2/3/4): "))

        if userInput == 1:
            stud = addData()
            SaveData(stud.toFile())
        elif userInput == 2:
            print("-----Printing Data-----")
            viewAll()
        elif userInput == 3:
            roll = int(input("Enter Roll Number to remove: "))
            removeData(roll)
        elif userInput == 4:
            print("Thank you for Visiting...")
            break
        else:
            print("Invalid choice, try again!")


menu()
