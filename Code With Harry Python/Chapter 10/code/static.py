class employee:
    name = "Rajat"
    language = "python" # this is an class attribute 
    salary = 1200000
# data is an object attribute
    @staticmethod
    def greet():
        print(f"Good morning")
    def info(self):
        print(f"The language is {self.language} and His salary is {self.salary}")
data = employee()
data.name = "Rajat"# this is an instance attribute

data.greet()
print(data.name , data.salary , data.language)
data.info()

'''
Sometimes we need a function that does not use the self-parameter. We can define a 
static method like this: 
'''