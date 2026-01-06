# Create a simple calculator using conditionals (+, -, *, /).


a = int(input("Enter a number: " ))

operator = input("Enter what type of operator you want (+,-,*,/): ")

b = int(input("Enter a number: " ))

plus = (a + b)
min = (a - b)
mul = (a * b)
div = (a/+ b)
if(operator == "+" ):
    print(f" {a} + {b} is {plus}")
elif(operator == "-" ):
    print(f" {a} - {b} is {mul}")
elif(operator == "*" ):
    print(f" {a} * {b} is {mul}")
elif(operator == "/" ):
    print(f" {a} / {b} is {div}")
else:
    print("Error")