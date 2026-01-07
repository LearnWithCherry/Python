class employee:
    name = "Rajat"
    language = "python" # this is an class attribute 
    salary = 1200000
# data is an object attribute
    def greet(self):
        print(f"Good morning")
    def info(self):
        print(f"The language is {self.language} and His salary is {self.salary}")
data = employee()
data.name = "Rajat"# this is an instance attribute

data.greet()
print(data.name , data.salary , data.language)
data.info()
