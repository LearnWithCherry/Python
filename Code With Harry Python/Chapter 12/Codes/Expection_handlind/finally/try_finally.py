def prg():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("We are inside Finally!!")

prg()

def prg():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return

    print("We are inside Finally!!")

prg()



# if u want to print any thing but it is inside a function and the program crashes it will not run 
# but using finally will help to run that code even if the program fails

# ✅ finally in Python
# The finally block is always executed, no matter what —
# even if there's an error ⚠️ or the program returns early.

# if i want to print anything after return it will not print when it is inside the function so
# we use finally to print that when the program crashses

# as we can see the both the program