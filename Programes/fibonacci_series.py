fib = int(input("Enter A Number: "))
a = 0
b = 1
if(fib == 1):
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,fib+1):
        c = a+b
        a = b
        b = c
        print(c)
