# def greet():
#     user = input("Enter your name: ")
#     print(f"Hello\nGood Morning {user}")    
# greet()

# def avg():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     c = int(input("Enter a number: "))
#     print((a+b+c)/3)

# avg()
           
# def gd(name, end = "Thanks"):
#     print("Good Day "+name+"\n\t"+end)

# gd("Rajat")
# gd("Rohan","Thank You")
# gd("Rihu","Thank You")

# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * fact(n-1)

# n = int(input("Enter a number: "))
# print(f"Factorial of {n} is: {fact(n)}")


# problems 
def gr8():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    if (a > b and a > c):
        print("A is Greater.")
    elif(b > a and b > c):
        print("B is Greater.")
    elif(c > a and c > b):
        print("C is Greater.")
    else:
        print("Error")

# gr8()

# print("Hello",end="")
# print("a")
# print("b")
# print("c",end="")
# print("d",end="")

# def num(n):
#     if n == 0 or n == 1:
#         return 1
#     return num(n-1) + n
# n = int(input("Enter a number: "))
# print(f"Sum of {n} Natural Number are {num(n)}")

def pattern(n):
    if (n == 0):
        return 
    print("*"*n)
    pattern(n-1)
n = int(input("Enter a number: "))
pattern(n)