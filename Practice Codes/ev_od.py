def EvenOdd():
    while True:
        number = input("Enter a number: ")
        if number == ".":
            break
        else:
            if(int(number) % 2 == 0):
                print(f"{number} is Even")
            else:
                print(f"{number} is Odd")

EvenOdd()