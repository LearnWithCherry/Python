import random

def game():
    print("Welcome to the game!")

    # Step 1: Read high score (assumes file exists and has a number)
    with open("09_file_Input_&_output//problems//2//hi_score.txt", "r") as f:
        hi_score = int(f.read())

    # Call the main game logic
    hi_score = valid_choice(hi_score)

    # Show final score
    print(f"Your high score: {hi_score}")

def valid_choice(hi_score):
    computer = random.randint(1, 50)
    choose = int(input("Enter a number from 1 to 50: "))
    
    if choose > 50 or choose < 1:
        print("Invalid Number!!")
        return hi_score  # Don't change score if invalid

    print(f"Computer chose: {computer}")

    if choose == computer:
        print("Draw!!")
    elif choose > computer:
        print("You win!")
        hi_score += 1
        with open("09_file_Input_&_output//problems//2//hi_score.txt", "w") as f:
            f.write(str(hi_score))
    else:
        print("Computer won!")

    return hi_score

# Start the game
game()
