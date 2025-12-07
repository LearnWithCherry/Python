Nterm = int(input("Enter number of terms: "))

result = list(map(lambda x : 2 ** x, range(Nterm + 1)))

for i in range (Nterm + 1):
    print("Value of 2 raised to power", i, "is" , result[i]) 