 # Inheritance is a way of creating a new class from an existing class. 

class employee():
    company = "ITC"
    def show(self , name , salary):
        self.name = name 
        self.salary = salary
        print(f"The name is {self.name} and the salary is {self.salary}")
class coder(employee):
    language = "Python"
    def used_language(self):
        print(f"The langauge we use the most is {self.language}")
class programmer(coder , employee):
    company = "Info Tech"
    def showLanguage(self):
        print(f"The name of the employee is {self.name} and he is a {self.language} expert \nHe works in {self.company}")


a = programmer()


a.show("Rajat" , 1500000)
a.used_language()
a.showLanguage()