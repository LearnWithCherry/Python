def total():
    filename = "18_Projects\\01_Small_projects\\TXT_files\\total.txt"
    try:
        with open(filename , 'r') as file:
            content = file.read()
            s = content.split()
            x = len(s) # for total lenght 
            print(x)
    except FileNotFoundError:
        print("File not found")
total()