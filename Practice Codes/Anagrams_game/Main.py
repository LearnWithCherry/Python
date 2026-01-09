# Jumble word game 
import random
def game():
    words = ["ironman","thor","hulk","wanda","captainamerica","vision","thanos"]

    word = random.choice(words)
    jumble = "".join(random.sample(word, len(word)))
    print(jumble)
    tries = 5 

    while(tries != 0):
        print("~"* 30)
        user = input("Enter your Guess: ").lower()
        print("Welcome To The Jumble Word Game")
        if word == user:
            print("You Guessed it right...")
            ask = input("Press Enter to play Again or NO to exit: ").lower()
            if ask == "":
                return game()
            elif ask == "no":
                print("Thanks for playing....")
                break
        else:
            print("You Guessed it Wrong try again..")
            tries -= 1
    else:
        print("You all tries Finished")
        print("The Word was",word)
game()