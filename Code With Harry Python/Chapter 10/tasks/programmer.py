class programmer:
    company = "Microsoft"
    def __init__(self , name , age , position , salary , work):

        self.name     =   name
        self.age      =   age 
        self.position =   position 
        self.salary   =   salary
        self.work     =   work 
c = programmer("Rajat" , 20 , "senior AI & Ml engineer" , 1500000 , "developing Ai")
print(c.company , c.name , c.age , c.position , c.salary , c.work)