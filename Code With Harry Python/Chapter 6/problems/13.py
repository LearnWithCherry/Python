# Input: lengths of the three sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# First, check if it can form a triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    # Check for Equilateral
    if a == b == c:
        print("This is an Equilateral Triangle.")
    # Check for Isosceles
    elif a == b or b == c or a == c:
        print("This is an Isosceles Triangle.")
    # Otherwise, it's Scalene
    else:
        print("This is a Scalene Triangle.")
else:
    print("These sides do NOT form a valid triangle.")


'''
🔺 Types of Triangles by Sides
Equilateral Triangle
✅ All three sides are equal

✅ All angles are 60°

Looks like a perfect triangle!

Example: If all sides = 5 cm → Equilateral

Isosceles Triangle
✅ Two sides are equal, one is different

✅ The angles opposite the equal sides are also equal

Example: Sides = 5 cm, 5 cm, 3 cm → Isosceles

Scalene Triangle
❌ No sides are equal

❌ All angles are different

Example: Sides = 4 cm, 5 cm, 6 cm → Scalene

'''