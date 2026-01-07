class calculator:
    def __init__(self , n ):
            self.n = n

    def square(self):
        print(f"Square is {self.n * self.n}")

    def cube(self):
        print(f"Cube is {self.n ** 3}")

    def Square_root(self):
        print(f"Square root is {self.n ** 0.5}")

a = calculator(5)
a.square()        
a.cube()
a.Square_root()