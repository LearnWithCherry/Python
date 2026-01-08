class School:
    def __init__(self, name: str): # name: str is a type hint — it tells Python and other developers that name should be a string.
        self.name = name # This saves the name of the school in an instance variable.
        self.classes = None # They’ll be filled later using setter methods. 
        self.teachers = None 
        self.students = None

    def set_classes(self, number_of_classes: int):
        if number_of_classes > 0: #Takes number of classes as input.If it's positive (> 0), it sets the value:
            self.classes = number_of_classes

    def set_teachers(self, total_teachers: int):
        if total_teachers >= 0:#Takes number of classes as input.If it's positive (> 0), it sets the value:
            self.teachers = total_teachers

    def set_students(self, total_students: int):
        if total_students >= 0:#Takes number of classes as input.If it's positive (> 0), it sets the value:
            self.students = total_students

    def __str__(self):
        details = f" School Name: {self.name}\n"
        if self.classes is not None: #This makes sure we only print values that are actually set.
            details += f" Total Classes: {self.classes}\n"
        if self.teachers is not None:#This makes sure we only print values that are actually set.
            details += f" Total Teachers: {self.teachers}\n"
        if self.students is not None:#This makes sure we only print values that are actually set.
            details += f" Total Students: {self.students}\n"
        return details.strip()

# Example usage
s = School("School of Success")
s.set_classes(30)
s.set_teachers(50)
s.set_students(500)

print(s)
try:
    with open("library.txt", "a") as f:
        f.write(str(s))

except FileNotFoundError:
    print("error")
