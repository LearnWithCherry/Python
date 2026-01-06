# Check if a number is divisible by 3 and 5.
a = int(input("Enter a number: "))

if(a % 3 == 0 ):
    print(f"3 is divisable by {a}")
else:
    print("This number cannot be divided by 3")

b = int(input("Enter a number: "))

if(b % 5 == 0 ):
    print(f"5 is divisable by {b}")
else:
    print("This number cannot be divided by 5")

