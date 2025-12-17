# year = int(input("Enter year that you want to check: "))
# if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
#     print("Its a leap year.")    
# else:
#     print("Its not a leap year.")
check = int(input("Press 1 to get Leap year list.\nPress 2 to get non Leap year list.\nEnter: "))

if check == 1:
    for i in range(1900, 2025):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            print("Leap year list: ", i)
else:
    for i in range(1900, 2025):
        if not (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)):
            print("Non Leap year list: ", i)
