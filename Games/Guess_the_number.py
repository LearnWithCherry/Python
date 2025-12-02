import random
import time 

def game(name=None):
    if name is None:
        name = input("Please Enter your Name: ")

    print(f"Welcome To The Game {name}!")
    max_attempts = int(input(f"Enter how Many Attempts you want {name}: "))
    print("------------------------------------------")
    level = input("Enter which level you want to play (easy/normal/hard): ").strip().lower()
    if level == "easy":
        limit = 20
    elif level == "normal":
        limit = 50
    elif level == "hard":
        limit = 100
    computer = random.randint(1 , limit)
    attempt = 0
    start_time = time.time()
    while attempt < max_attempts:
        attempt +=1
        print(f"Its Your Attemp {attempt} out of {max_attempts} Attempts")
        
        try:
            # print(f"computer chose = {computer} for checking ! remove if you see this ")
            you = int(input(f"👉 Enter your guess {name}(1 to {limit}): "))
            if you < 1 or you > limit:
                print(f"⚠️ Please enter a number between 1 and {limit} only!")
                continue
        except ValueError:
            print("🚫 Invalid input! Please enter a number.")
            continue
        if computer == you:
            print("------------------🎊Congrats🎊-------------------")
            print(f"You won {name} \nYou Gussed it Right. It was {computer}!")
            end_time = time.time()
            time_taken = round(end_time - start_time)
            print(" ")
            print(f"Time taken to compelete is {time_taken} Seconds ⏱")
            break
        elif computer > you:
            print("------------------------------------------")
            print(" ")
            print(f"Guess Higher ⬆️ Number {name} ")
        elif computer < you:
            print("------------------------------------------")
            print(" ")
            print(f"Guess Lower ⬇️ Number {name} ")
        else:
            print("------------------Sorry-------------------")
            print(" ")
            print(f"Sorry {name} you lose, It was {computer}")
        print(" ")
            
    print(f"------------------One-More-Game-{name}------------------")
    play = input(f"Do you want to play Again {name}(yes/no): ").strip().lower()
    if play == "yes":
        return game(name)
    else:
        print(f"Thank You for playing {name} ")
game()