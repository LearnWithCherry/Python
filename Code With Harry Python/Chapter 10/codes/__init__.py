class employee:
    def __init__(self , name , salary , language ):
        self.name = name
        self.salary = salary
        self.language  = language 
        print("Hi\n This is an object")

rajat = employee("Rajat" , 1500000 , "Python")

print(rajat.name , rajat.salary , rajat.language )