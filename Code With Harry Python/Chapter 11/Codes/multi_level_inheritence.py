'''
What is Multilevel Inheritance?
Multilevel inheritance means a class inherits from a class, which itself inherits from another class — like a chain.

class B inherits from A

Class C inherits from B

So, C gets access to all members of B and A

'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: ₹{self.salary}")


class Coder(Employee):  # Coder inherits from Employee
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_language(self):
        print(f"{self.name} codes in {self.language}")


class Programmer(Coder):  # Programmer inherits from Coder
    def __init__(self, name, salary, language, project):
        super().__init__(name, salary, language)
        self.project = project

    def show_project(self):
        print(f"{self.name} is working on project: {self.project}")


# Creating an object of the last class in the chain
p1 = Programmer("Rajat", 1500000, "Python", "AI Assistant")

# Accessing all inherited methods
p1.show_details()
p1.show_language()
p1.show_project()


'''
📘 Key Concepts:
super().__init__() calls the constructor of the parent class.

Class Programmer has access to:

Employee methods (from grandparent class)

Coder methods (from parent class)
'''