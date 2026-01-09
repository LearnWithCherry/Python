class Record:
    def __init__(self, name, subject, marks):
        self.name = name
        self.subject = subject
        self.marks = marks    
    
    def __str__(self):
        return (f"Name of the student is: {self.name}\n"
                f"{self.name} scored {self.marks} marks in {self.subject}!\n")

    def to_file(self):
        return f"{self.name},{self.subject},{self.marks}\n"

    @staticmethod
    def from_file(contentInFile):
        parts = contentInFile.strip().split(',')
        if len(parts) == 3:
            return Record(parts[0], parts[1], parts[2])
        return None

# ----------------------------------------------------

def studentData():
    name = input("Enter student Name: ")
    subject = input("Enter subject Name: ")

    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("❌ Invalid marks input. Must be a number!")
        return

    student = Record(name, subject, marks)

    try:
        with open("18_Projects\\Students_marks_records\\data.txt", "a") as f:
            f.write(student.to_file())
        print("✅ Student data saved successfully.")
    except FileNotFoundError:
        print("❌ No file found. Please check your file path!")

# ----------------------------------------------------

def shwData():
    try:
        with open("18_Projects\\Students_marks_records\\data.txt", "r") as f:
            for contentInFile in f:
                student = Record.from_file(contentInFile)
                if student:
                    print(student)
    except FileNotFoundError:
        print("❌ File not found!")

# ----------------------------------------------------

def checkFile():
    try:
        with open("18_Projects\\Students_marks_records\\data.txt", "r") as f:
            content = f.read()
            if not content.strip():
                return False
            return True
    except FileNotFoundError:
        return False

# ----------------------------------------------------

def menu():
    while True:
        print("\n--- Welcome to Student Report Card ---")
        print("1. Add Student Details")
        print("2. Show All Student Details")
        print("3. Exit Menu")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("⚠️ Please enter a valid number (1-3)!")
            continue

        if choice == 1:
            studentData()
        elif choice == 2:
            if checkFile():
                shwData()
            else:
                print("📂 Sorry, there is no data to show.")
        elif choice == 3:
            print("👋 Thank you for using the system! Bye...")
            break
        else:
            print("❌ Invalid option. Please choose from 1 to 3.")

# ----------------------------------------------------

if __name__ == "__main__":
    menu()
