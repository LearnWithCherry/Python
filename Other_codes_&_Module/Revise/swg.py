import random

def game():
    computer_points = 0
    your_points = 0

    while True:
        computer = random.randint(0, 2)
        you = int(input("\n ---Choose---\nRock     -   0\nPaper    -   1\nScissors -   2\nExit     -   3\n")) 

        if you == 3:
            print("\nGame Over")
            print("Your points:", your_points)
            print("Computer points:", computer_points)
            break

        if computer == you:
            print("It's a Draw")

        elif computer == 0 and you == 2:
            print("Rock breaks Scissors\nComputer gets a point")
            computer_points += 1

        elif computer == 2 and you == 0:
            print("Rock breaks Scissors\nYou get a point")
            your_points += 1

        elif computer == 1 and you == 0:
            print("Paper covers Rock\nComputer gets a point")
            computer_points += 1

        elif computer == 0 and you == 1:
            print("Paper covers Rock\nYou get a point")
            your_points += 1

        elif computer == 2 and you == 1:
            print("Scissors cuts Paper\nComputer gets a point")
            computer_points += 1

        elif computer == 1 and you == 2:
            print("Scissors cuts Paper\nYou get a point")
            your_points += 1

game()
