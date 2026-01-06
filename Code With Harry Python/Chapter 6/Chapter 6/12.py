# Find the largest among three numbers.

a = int(input("Enter a number: " ))

b = int(input("Enter a number: " ))

c = int(input("Enter a number: " ))

if(a>b and a>c):
    print(f"A is greater!")
elif(b>a and b>c):
    print(f"B is greater!")
else:
    print(f"C is greater!")
