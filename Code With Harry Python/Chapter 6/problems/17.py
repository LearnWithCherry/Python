# takes input and tell +ve , -ve or 0

a = int(input("Enter a Number: "))

if(a >= 1 ):
    print(f"{a} is an Positive Integer ")
elif(a <= -1):
    print(f"{a} is an Negative Integer")
elif( a == 0):
    print(f"{a} is Zero")