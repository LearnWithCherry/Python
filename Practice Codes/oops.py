class employee:
    name = "default"
    age = "0"
    sex = "not defined"
    # def greet():
        # print("Good Morning") #"Self is required here other vise error will be there"
    def getinfo(self):
        print(f"The name of the employee is: {self.name}",
              f"\nThe age of the employee is: {self.age}",
              f"\nThe sex of the employee is: {self.sex}",)
    @staticmethod
    def greet():
        print("Good Morning") # Marking function as self it does not required self
rajat = employee() 
rajat.name = "Rajat"
rajat.age = "19"
rajat.sex = "Male"
# print(rajat.name,rajat.age, rajat.sex)
# rajat.getinfo()


# __init__

class one:
    name = ""
    age = ""
    def __init__(self, name, age): # dunder method (called automatically)
        self.name = name
        self.age = age
        # print("init is called")
        
    def details(self):
        print(f"Name of the Employee is: {self.name}",
              f"\nName of the age is: {self.age}")
        
rajat = one("Rajat","19")
# rajat.name = "Rajat"
# rajat.age = "19"
# rajat.details()


class programmer:   
    name = ""
    age = ""
    role = ""
    salary = ""
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary
    def details(self):
        print(f"Name of the employee is {self.name}",
              f"\nAge of {self.name} is {self.age}",
              f"\nRole of {self.name} is {self.role}",
              f"\nSalary of {self.name} is {self.salary}")
        
rajat = programmer("Rajat", "19", "AI dev", "120000")
# rajat.details()
print("")
ruham = programmer("Ruham", "19", "software dev", "150000")
# ruham.details()
print("")
nidhi = programmer("Nidhi", "19", "R&D Manager", "110000")
# nidhi.details()

class calc:
    def __init__(self, n):
        self.n = n
    @staticmethod
    def greet():
        print("--Welcome--")
    def square(self):
        print(f"The square is {self.n * self.n}")
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")
    def root(self):
        print(f"The root is {self.n ** 0.5}")

# a = calc(4)
# a.greet()
# a.square()
# a.cube()
# a.root()

        
