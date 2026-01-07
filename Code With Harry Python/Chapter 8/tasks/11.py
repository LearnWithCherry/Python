def show():
    x = 10  # local
    print(x)

x = 5  # global
show()
print(x)


# first global variable will print then local will