word = "Artificial intelligence and machine learning"

reverse = word[::-1]

tries = 5
while(tries != 0):
    print("Reversed string: ",reverse)
    user = input("Guess whjat it could be: ")
    if user == "Artificial intelligence and machine learning":
        print("You guessed it Right")
        break
    else:
        print("No its wrong")
        tries -= 1
        print("you all tries Finished....")