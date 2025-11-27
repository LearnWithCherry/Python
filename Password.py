
import string
def password():
    # password check block
    w = input("Enter Website name💻: ")
    p = input("Enter password🔐: ")

    has_upper = has_lower = has_digit = has_special = False
    special_characters = string.punctuation 

    # checking is password is strong enough
    for char in p:
        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if char.isdigit():
            has_digit = True

        if char in string.punctuation:
            has_special = True

    # telling user is missing
    if not has_upper:
        print(f"Forgot to add Upper case Character {p}🔠!! ")
        print("-" * 30 +"\n")
        return password()
    elif not has_lower:
        print(f"Forgot to add Lower case Character {p}🔡!! ")
        print("-" * 30 + "\n")
        return password()
    elif not has_digit:
        print(f"Forgot to add Digits {p}🔢!! ")
        print("-" * 30 + "\n")
        return password()
    elif not has_special:
        print(f"Forgot to add Special Character {p}⁉️")
        print("-" * 30 + "\n")
        return password()
    else:
        print("You are good To Go☑️!!!")

    # strength block
    strength = 0
    if(len(p) >= 8): strength += 1
    if has_upper: strength += 1
    if has_lower: strength += 1
    if has_digit: strength += 1
    if has_special: strength += 1

    # tell user password its strength 
    if(strength == 5):
        print("Your password is Very strong💪!!")
    elif(strength > 3):
        print("Strength is not that high👎👎!!")
        return password()
    elif(strength > 1):
        print("Password is Very weak👎👎!!")
        return password()
    
    # save password!!!
    try:
        with open("18_Projects\\Data.txt", "a") as f:

            f.write(f"Name of the is Website: {w}\n")
            f.write(f"Password is: {p}\n")
            f.write("-" * 30 + "\n")
    except FileNotFoundError:
        print("file not found check Again❌❌!!!")

def shw_psw(): # show saved data
    try:
        with open("18_Projects\\Data.txt", "r") as f:
            print("Printing data....📑")
            content = f.read()
            print(content)

    except FileNotFoundError:
        print("file not found check Again❌❌!!!")

def options():# printing options

    while True:
        print("Welcome to Google💻")
        print("Enter\n1 To Add website and Password\n2 To see saved Password\n3 To Exit")
        try:
            o = int(input("Enter What you want(1/2/3): "))
        except ValueError:
            print("Chose correct Option!")
            return options

        if o == 1:
            return password()
        elif o == 2:
            return shw_psw()
        elif o == 3:
            print("Bye Bye...👋👋\nVisit Again!!")
            break
        else:
            print("Error❌❌")
options()
