

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if(b == 0):
    raise ZeroDivisionError("\n-----Program cannot Divide Number by zero!!-----")
else:
    print(f"the division a/b is {a/b}")
