class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def compute_tax(self):
        return self.salary * 0.1 if self.salary > 50000 else 0

    def save_details(self):
        with open('employees.txt', 'a') as f:
            f.write(f"{self.name},{self.salary},{self.compute_tax()}\n")

while True:
    print("\n1. Add Employee  2. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        emp = Employee(input("Name: "), float(input("Salary: ")))
        emp.save_details()
    elif choice == '2':
        break
    else:
        print("Invalid choice!")
