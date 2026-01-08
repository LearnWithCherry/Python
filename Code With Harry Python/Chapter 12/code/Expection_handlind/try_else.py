try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("If you can see this that means you passed try block")