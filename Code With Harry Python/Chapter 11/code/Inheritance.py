# Inheritance is a way of creating a new class from an existing class. 

class employee():
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class programmer(employee):
    company = "Info Tech"
    def showLanguage(self):
        print(f"The name of the employee is {self.name} and he is a {self.language}")

a = employee()
b = programmer()

print(a.company , b.company)