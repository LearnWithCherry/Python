def calc(a,b,o):
    if(o == "-"):
        return a - b
    elif(o == "+"):
        return a + b
    elif(o == "/"):
        return a / b
    elif(o == "*"):
        return a * b
    else:
        print("Error..")

o = input("Enter Operator: ")
a = int(input("Enter A:"))
b = int(input("Enter B:"))

print(calc(a,b,o))