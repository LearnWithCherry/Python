try:
    a = int(input("Enter a number: "))
    print(a)

# except Exception as e:
#     print(e)

except ValueError as v:
    print(v)
    print("oyee, Number bola hai!!")

print("Program Is Running !!")  

# An exception is an error that stops your program
#  if you don’t handle it.
