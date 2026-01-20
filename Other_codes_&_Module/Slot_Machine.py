# import random
# import turtle
# import time
   
import random

def spin_reels():
    symbols = ["🍒", "🍋", "🔔", "💎", "🍊"]
    return [random.choice(symbols) for _ in range(3)]

def check_win(reels):
    return reels[0] == reels[1] == reels[2]

def slot_game():
    coins = 100  # Starting balance
    print("🎰 Welcome to the Slot Machine!")
    print("🎯 Match all 3 symbols to win 50 coins! Each spin costs 10 coins.")
    
    while coins >= 10:
        input("\n🔁 Press Enter to spin...")
        coins -= 10

        reels = spin_reels()
        print(" | ".join(reels))

        if check_win(reels):
            print("🎉 JACKPOT! You won 50 coins!")
            coins += 50
        else:
            print("😢 No match. Try again!")

        print(f"💰 Your current balance: {coins} coins")
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    if coins < 10:
        print("🪙 Not enough coins to play. Game Over!")

    print(f"🏁 Final Balance: {coins} coins\nThanks for playing!")

# Run it
slot_game()
