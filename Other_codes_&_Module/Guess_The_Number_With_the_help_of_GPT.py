import random
import time

high_score = 0  # Global for session

def game(name=None):
    global high_score

    if name is None:
        name = input("Please Enter Your Name: ")

    print(f"\n🎉 Welcome to the Guess the Number game, {name}!")
    print("----------------Attempts--------------------------------")
    max_attempts = int(input("🎯 How many attempts do you want? "))

    print("----------------LEVEL--------------------------------")
    level = input("🧠 Choose difficulty (Easy/Mid/Hard): ").strip().lower()

    if level == "easy":
        upper_limit = 10
    elif level == "mid":
        upper_limit = 25
    elif level == "hard":
        upper_limit = 50
    else:
        print("⚠️ Invalid level! Defaulting to Easy.")
        upper_limit = 10

    computer = random.randint(1, upper_limit)
    print(f"[DEBUG] Computer chose: {computer}")  # For debugging

    attempt = 1
    start_time = time.time()  # Start timer

    while attempt <= max_attempts:
        print(f"\n🕹️ Attempt {attempt} out of {max_attempts}")
        try:
            you = int(input(f"👉 Enter your guess (1 to {upper_limit}): "))
            if you < 1 or you > upper_limit:
                print(f"⚠️ Please enter a number between 1 and {upper_limit} only!")
                continue
        except ValueError:
            print("🚫 Invalid input! Please enter a number.")
            continue

        if you == computer:
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)

            print("----------------RIGHT--------------------------------")
            print(f"🎊 You guessed it right in {attempt} attempts!")
            print(f"⏱️ Time taken: {time_taken} seconds")

            score = max(0, 100 - (attempt - 1) * 10)
            print(f"🏆 Your Score: {score}")

            if score > high_score:
                high_score = score
                print("🔥 NEW HIGH SCORE!")
            else:
                print(f"🥈 High Score to beat: {high_score}")

            break
        elif you < computer:
            print("----------------TRY AGAIN--------------------------------")
            print("⬆️ Try a higher number.")
        else:
            print("----------------TRY AGAIN--------------------------------")
            print("⬇️ Try a lower number.")

        attempt += 1
    else:
        print(f"\n💥 Game Over! The correct number was {computer}. Better luck next time!")
        print("🏆 Score: 0")

    p = input("\n🔁 Do You Want to Play Again (Yes/No): ").strip().lower()
    if p == "yes":
        return game(name)
    else:
        print(f"Thank You For Playing, {name} 🌟\n🏁 Final High Score: {high_score}")

# Start the game
game()
