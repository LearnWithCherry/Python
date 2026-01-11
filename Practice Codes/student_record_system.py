# student_record.py

def add_student(students):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully.")


def save_to_file(students):
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['roll']},{s['marks']}\n")
    print("Data saved to file.")


def load_from_file():
    students = []
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, roll, marks = line.strip().split(",")
                students.append({"name": name, "roll": roll, "marks": marks})
    except FileNotFoundError:
        pass
    return students


def show_students(students):
    for s in students:
        print(s)


def search_student(students):
    roll = input("Enter roll to search: ")
    for s in students:
        if s["roll"] == roll:
            print("Student found:", s)
            return
    print("Student not found.")


students = load_from_file()

while True:
    print("\n1.Add  2.Show  3.Search  4.Save  5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        show_students(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        save_to_file(students)
    elif choice == "5":
        save_to_file(students)
        break
    else:
        print("Invalid choice")
