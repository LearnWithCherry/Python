
def tables():
    try:
        n = int(input("Enter a Number: "))
        with open("15_Daily_Questions\\tables.txt", "a") as f:
            for i in range(1,11):
                table = (f"Multiplying {n} x {i} = {n*i}\n")
                f.write(table)
    except FileNotFoundError:
        print("File is Missing ")
tables()