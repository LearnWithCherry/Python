class Complex:
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __sub__(self, c2):
        return Complex(self.r - c2.r, self.i - c2.i)

    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __truediv__(self, c2):
        denom = c2.r**2 + c2.i**2
        real = (self.r * c2.r + self.i * c2.i) / denom
        imag = (self.i * c2.r - self.r * c2.i) / denom
        return Complex(real, imag)

    def __str__(self):
        sign = '+' if self.i >= 0 else '-'
        return f"{self.r} {sign} {abs(self.i)}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)

print("Addition of c1 + c2 =", c1 + c2)
print("Subtraction of c1 - c2 =", c1 - c2)
print("Multiplication of c1 * c2 =", c1 * c2)
print("Division of c1 / c2 =", c1 / c2)
