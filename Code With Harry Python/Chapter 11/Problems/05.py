class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.y,self.z + other.z)

    def __mul__(self, other):
        # Dot product
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Use your class objects, not tuples
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print("v1 + v2 =", v1 + v2)     # Vector(5, 7, 9)
print("v1 • v2 =", v1 * v2)     # Dot product: 1*4 + 2*5 + 3*6 = 32

print("v1 + v3 =", v1 + v3)     # Vector(8, 10, 12)
print("v1 • v3 =", v1 * v3)     # Dot product: 1*7 + 2*8 + 3*9 = 50
