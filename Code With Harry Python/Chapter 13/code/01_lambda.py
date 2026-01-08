# lambda is a way to write small, anonymous functions
# (functions without a name) in a single line.
# syntax:
# lambda arguments: expression

square = lambda X: X*X

print(square(11111115))

# ✅ Regular Function vs Lambda
# 🔸 Normal Function:

def square(x):
    return x * x

print(square(5))  
# Output: 25
# 🔸 Same using Lambda:

square = lambda i: i * i

print(square(5)) 
# Output: 25

# when not to use it:  When the function is complex or reused often.

cube = lambda c: c ** 3

print(cube(3))

'''1. Square of a number
square = lambda x: x * x

2. Check if number is even
is_even = lambda x: x % 2 == 0

3. Get last character of a string
last_char = lambda s: s[-1]
'''

# print names length wise !!
names = ["Cherry", "AI", "Python", "Machine", "Code"]

sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)
