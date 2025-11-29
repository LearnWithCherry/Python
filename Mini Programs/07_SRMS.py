
class SRMS:
    
    def __init__(self, name , Age , Year , roll_number , CGPA , course ):
        self.name = name
        self.Age = Age
        self.Year = Year 
        self.roll_number = roll_number
        self.CGPA = CGPA
        self.course = course

    def saveFile(self):
        return f"{self.name} , {self.Age} , {self.Year} , {self.roll_number} , {self.CGPA} , {self.course}"
    
def AddData():
    name = input("Enter Students name: ")
    Age = int(input("Enter Students Age: "))
    Year = int(input("Enter Students year: "))
    roll_number = int(input("Enter Students RL: "))
    CGPA = float(input("Enter Students CGPA: "))
    course = input("Enter Students course: ")
    student = SRMS(name , Age , Year , roll_number , CGPA , course )
    return student

def saveData(student):
    filenmame = "15_Daily_Questions\\project_txt_file\\05_SRMS.txt"
    try:
        with open (filenmame, "a") as file:
            file.write(student.saveFile())
            print("-----Data saved-----")
    except FileNotFoundError:
        print("NO file found")

def view_all():
    filenmame = "15_Daily_Questions\\project_txt_file\\05_SRMS.txt"
    try:
        with open(filenmame, "r") as f:
            content = f.read()
            if content == "":
                print("--- No Content In file Sorry ---")
            else:
                print(content)
    except FileNotFoundError:
        print("-----No file found-----")

def menu():
    print("-----Welcome----")
    while True:
        print("1 = Add Data\n2 = View All\n3 = exit ")
        n = int(input("Enter choice: "))
        if n == 1:
            student = AddData()
            saveData(student)
        elif n == 2:
            view_all()
        elif n == 3:
            print("------Thanku for visiting------")
            break

menu()