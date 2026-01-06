# Write a program to find the greatest of four numbers entered by the user. 

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if(a>b and  a>c and  a>d):
    print(f"{a} is greater!!!")
elif(b>a and  b>c and  b>d):
    print(f"{a} is greater!!!")
elif(c>a and  c>c and  c>d):
    print(f"{a} is greater!!!")
elif(d>a and  d>b and  d>c):
    print(f"{a} is greater!!!")
else:
    print("Error")