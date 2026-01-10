age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age >= 13 and age <= 18:
    print("Teen")
elif age >= 19 and age <= 100:
    print("Adult")
else:
    print("Invalid")