# Problem to solve !!!

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
         print(f"Name: {self.name} Age: {self.age}")

    def greet(self):
        print(f"Hello {self.name}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_info(self):
        print(f"Grade: {self.grade}")
        super().get_info()

class Teacher:
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        print(f"Teaching {self.subject}")

    def greet(self):
        print("Good morning class!")

class TA(Student, Teacher):
    def __init__(self, name, age, grade, subject):
        Student.__init__(self, name, age, grade)
        Teacher.__init__(self , subject)
    
    @staticmethod
    def help():
        print("Helping students...")

    def get_info(self):
        super().get_info()
        print(f"Subject: {self.subject}")

p = Person("Alex", 30)
s = Student("Ravi", 20, "A")
t = Teacher("Math")
ta = TA("Nina", 24, "B", "Physics")

print("\n--- Person ---")
p.greet()

print("\n--- Student ---")
s.get_info()

print("\n--- Teacher ---")
t.teach()

print("\n--- Teaching Assistant (TA) ---")
ta.get_info()
ta.help()

