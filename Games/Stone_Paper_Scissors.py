import random

def game():
    print("Welcome to the game 🎮")
    print("")
    want_name = input("Do you want to enter your name? (yes/no): ").lower()
    
    if want_name == "yes":
        name = input("Enter your name: ")
        print(f"Welcome {name} to the game.\nI hope you enjoy!! 😄")
    else:
        name = "You"
        print("No worries, let's continue!!")
    print("")

    options = {
        "a": "stone",
        "b": "paper",
        "c": "scissors"
    }
    computer_input = random.choice(['a', 'b', 'c'])
    computer_choice = options[computer_input]

    # print(f"\n💻 [DEV MODE] Computer already chose: {computer_choice}")
    print(" a = Stone \n b = Paper \n c = Scissores ")
    print("------------choose------------")
    user_input = input("Enter your choice (a/b/c): ").lower()
    user_choice = options[user_input]
    
   

    print("\n------- Result -------")
    print(f"💻 Computer chose: {computer_choice}")
    print(f"🧑 {name} chose: {user_choice}\n")

    if computer_choice == user_choice:
        print("😐 It's a draw!")
    elif (computer_choice == "stone" and user_choice == "paper") or \
         (computer_choice == "paper" and user_choice == "scissors") or \
         (computer_choice == "scissors" and user_choice == "stone"):
        print(f"🎉 {name} wins!")
    else:
        print("💻 Computer wins!")
    play = input("Do you want to play again (yes/no): ")
    if(play == "yes"):
         print("🔁 Restarting game 🎮")
         game()
    else:
        print("Thank You for playing \n---bye bye👋---")# Run the game
game()


































