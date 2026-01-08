
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        print(f"Two D vector = {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
        print(f"Three D vector = {self.i}i + {self.j}j + {self.k}k")

# Create a 2D vector
v2 = TwoDVector(1, 2)

# Create a 3D vector
v3 = ThreeDVector(4, 1, 5)
