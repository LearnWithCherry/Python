class animal():
    def __init__(self , name, type):
        self.name = name
        self.type = type

    def speak(self):
        print(f"{self.name} is a {type} and says Hello!")

class dog(animal):
    def __init__(self, name, breed):
        super().__init__(name , breed)
        self.breed = breed

    def speak(self):
        print(f"{self.name} is a {self.breed} dog. Woof!")

class Cat(animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):
        print(f"{self.name} is a {self.color} cat. Meow~")

a = animal("Generic", "Creature")
d = dog("Bruno", "Labrador")
c = Cat("Luna", "Black")

a.speak
d.speak()
c.speak()
