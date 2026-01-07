def grt():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    if(a>b and a>c):
        print(f"{a} is greatest!")
    elif(b>a and b>c):
        print(f"{b} is greatest!")
    elif(c>a and c>b):
        print(f"{c} is greatest!")

grt()