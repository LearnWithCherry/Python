def count():
    with open("15_Daily_Questions\\vowels.txt", "r") as f:
        content = f.read()
        print("There are in total",len(content))
        print(content.split())

count()
