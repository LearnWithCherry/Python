class employee:
    # name = "Rajat"
    language = "python" # this is an class attribute 
    salary = 1200000
# data is an object attribute
data = employee()
data.name = "Rajat"
print(data.name , data.salary , data.language)

data.name = "Aarush" # this is an instance attribute
data1 = employee()
print(data.name, data1.salary , data1.language)

'''
Here name is object attribute 
Salary and language are class attribute as they directly belonh to the class
'''