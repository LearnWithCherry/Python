class student:

    def __init__(self, name, age, standard):
        self.name = name
        self.age = age
        self.standard = standard

s = student("Cherry", 19, "B-tech Ai & Ml")
print(f"Name of the Student is {s.name} His age is {s.age} And His is in {s.standard} student")
