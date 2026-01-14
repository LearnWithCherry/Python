import random

def game():
    computer = random.randint(1, 100)

    with open("X:\\VScode\\PYTHON\\Other_Programs\\Revise\\data.txt", "r+") as file:
        score = file.read().strip()

        if score == "":
            score = 0
        else:
            score = int(score)

        print("Old High Score:", score)
        print("New Score:", computer)

        if computer > score:
            file.seek(0)                 
            file.write(str(computer))    
            file.truncate()
            print("New High Score Set!")
        else:
            print("Couldn't beat the High Score.")

game()
