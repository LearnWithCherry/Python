# check if a year is a leap year or not 

n = int(input("Enter a Year: "))

if(n % 4 == 0 and n % 100 != 0):
    print("Its a leap year ")
else:
    print("Its not")
