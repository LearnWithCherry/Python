import random

input("Press Enter to start")

while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = (dice1 + dice2)
    if total == 2:
            print(f"{total} Bad luck..🐍")
            break
    else:
            print(f"{total} Safe...")
            
