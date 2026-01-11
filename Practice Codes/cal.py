def calc():
    while True:
        o = input("Enter operator ('.' to Stop): ")
        if o == '.':
            break
        else:
            a = int(input("Enter First number: "))
            b = int(input("Enter Second number: "))
            if(o == '+'):
                print(f"The addition of {a} and {b} is {a+b}")
            elif(o == '-'):
                print(f"The subtraction of {a} and {b} is {a-b}")
            elif(o == '/'):
                print(f"The division of {a} and {b} is {a/b}")
            elif(o == '*'):
                print(f"The multiplicaton of {a} and {b} is {a*b}")
            else:
                print("Error Sorry.")

calc()
        