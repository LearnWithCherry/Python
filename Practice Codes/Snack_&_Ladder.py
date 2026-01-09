import random

# snakes and ladders mapping
snakes = {
    17: 7, 54: 34, 62: 19, 98: 79
}
ladders = {
    3: 22, 5: 8, 20: 29, 27: 56, 72: 91
}

def roll_dice():
    return random.randint(1, 6)

def check_snakes_ladders(position):
    if position in snakes:
        print(f"🐍 Oops! Snake at {position}, sliding down to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"🪜 Yay! Ladder at {position}, climbing up to {ladders[position]}") 
        return ladders[position]
    else:
        return position

def game():
    user = 0
    comp = 0
    
    print("---Welcome to Snack & Ladder---")
    while True:
        # ----- User's turn -----
        input("🎲 Your turn! Press Enter to roll: ")
        dice = roll_dice()
        user += dice
        if user > 100:   # don't cross 100
            user -= dice
        user = check_snakes_ladders(user)
        print(f"👉 You rolled {dice}, now at {user}")
        
        if user == 100:
            print("🎉 You Win!")
            break
        
        # ----- Computer's turn -----
        input("💻 Computer's turn... Press Enter to continue: ")
        dice = roll_dice()
        comp += dice
        if comp > 100:
            comp -= dice
        comp = check_snakes_ladders(comp)
        print(f"💻 Computer rolled {dice}, now at {comp}")
        
        if comp == 100:
            print("💻 Computer Wins!")
            break

game()  
