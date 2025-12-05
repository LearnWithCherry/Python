import string#-----------------------import special characters

# Function to add and check password strength
def psw():#-------------------------------function
    website = input("Enter Website name: ")#-------------------------------inputs from user
    password = input("Enter a password:")#-------------------------------inputs from user

    has_upper_character = has_lower_character = has_digit = has_special = False#-------------------------------flages
    special_characters = string.punctuation#-------------------------------mudules cantains special char

    for char in password:#-------------------------------loops throught each char and break each into single word

        if char.isupper:#-------------------------------check for upper case char
            has_upper_character = True#-------------------------------check if the condition is met not not

        if char.islower:#-------------------------------check for lower case char
            has_lower_character = True#-------------------------------check if the condition is met not not

        if char.isdigit:#-------------------------------check for digit in char
            has_digit = True#-------------------------------check if the condition is met not not

        if char in special_characters:#-------------------------------check for special char in char
            has_special = True #-------------------------------check if the condition is met not not

    #-------------------------------Feedback-----------------------------------------
    print("\nPassword Feedback:")

    if len(password) < 8:#-------------------------------check the lenght of password
        print("- Too short (minimum 8 characters required)")#-------------------------------if condition met this will prints
    if not has_upper_character:#-------------------------------if this condition did not met error will me generated
        print("- Add at least one UPPERCASE letter")#-------------------------------if condition met this will prints
    if not has_lower_character:#-------------------------------if this condition did not met error will me generated
        print("- Add at least one lowercase letter")#-------------------------------if condition met this will prints
    if not has_digit:#-------------------------------if this condition did not met error will me generated
        print("- Add at least one number")#-------------------------------if condition met this will prints
    if not has_special:#-------------------------------if this condition did not met error will me generated
        print("- Add at least one special character (like @, #, $, etc)")

    #Strength evaluation
    strength = 0#-------------------------------strength of the pass if 0 as default 
    if len(password) >= 8:      strength      += 1#------------------------------->increment with each condition met 

    if has_upper_character:     strength      += 1#------------------------------->increment with each condition met 

    if has_lower_character:     strength      += 1#------------------------------->increment with each condition met 

    if has_digit:               strength      += 1#------------------------------->increment with each condition met 

    if has_special:             strength      += 1#------------------------------->increment with each condition met 


    print("\nPassword Strength:", end=" ")#-------------------------------print Password Strength
    if strength == 5:#-------------------------------if all condition met prints strong pass and save it in the file 
        print("💪 Strong Password!")#-------------------------------if conditins is met this will print
        print("Password saved and Protected! 🔒")#-------------------------------if conditins is met this will print

        try:#-------------------------------try block if run sucessfully save data in file 
            with open("GPT_CODES//Password//password.txt", "a") as f:#-------------------------------add written website & password in .txt file
                f.write(f"Website: {website}\n")#-------------------------------if conditins is met this will print
                f.write(f"Password: {password}\n")#-------------------------------if conditins is met this will print
                f.write("-" * 30 + "\n")#-------------------------------if conditins is met this will print

        except FileNotFoundError:#-------------------------------other wise show error that file not found 
            print("❌ Folder not found! Make sure 'GPT_CODES//Password' exists.")#-------------------------------if conditins is met this will print

    elif strength >= 3:#-------------------------------if strength is less then 5 it return you to password blocks
        print("😐 Medium Strength")#-------------------------------if conditins is met this will print
        return psw()#-------------------------------return you to psw block
    
    else:#-------------------------------if strength is less then 5 it return you to password blocks
        print("❌ Weak Password")#-------------------------------if conditins is met this will print
        return psw()#-------------------------------return you to psw block
    
# Function to show saved data
def shw():#------------------------------- function

    try:#-------------------------------if there is a file named password then it will show the content of it otherwise prinis error
        print("\n------ Saved Passwords ------")#-------------------------------if conditins is met this will print
        with open("GPT_CODES//Password//password.txt", "r") as f:#-------------------------------show file data or content if present 
            content = f.read()#-------------------------------read file content 
            print(content)#-------------------------------prints file content 

    except FileNotFoundError:#-------------------------------print error
        print("❌ No password file found.")#-------------------------------if conditins is met this will print

# Menu function
def check():#-------------------------------function
    while True:#-------------------------------run the block untill there is an error or user exit program

        print("\n-- Menu --")#-------------------------------if conditins is met this will print
        print("1 = Add Website & Password")#-------------------------------if conditins is met this will print
        print("2 = Show added Website & Password")#-------------------------------if conditins is met this will print
        print("3 = Exit")#-------------------------------if conditins is met this will print

        try:#-------------------------------if wrong value enters then try will show error
            inp = int(input("Choose (1/2/3): "))

        except ValueError:#-------------------------------value error
            print("⚠️ Please enter a number (1, 2, or 3).")
            continue

        if inp == 1:#-------------------------------return to desire block here it is psw
            psw()#-------------------------------return to block

        elif inp == 2:#-------------------------------return to desire block here it is shw
            shw()#-------------------------------return to block

        elif inp == 3:#-------------------------------return to desire block here it is exit 
            print("Goodbye 👋")
            break#------------------------------- break the program 

        else:#-------------------------------if invalid char or num enters
            print("❌ Invalid option. Try again!")

# Start program
check()#-------------------------------runs the entire program

    