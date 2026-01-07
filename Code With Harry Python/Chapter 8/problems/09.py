def table():
    n = int(input("Enter whose table you want to see: "))
    i = 1
    for i in range(1,11):
        print(f"Table of {n} X {i} = {i * n}")
table()