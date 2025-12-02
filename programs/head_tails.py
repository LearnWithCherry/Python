import random

def coin():
    while True:
        coin_toss = (random.randint(0,1))
        input("press enter to Flip...🪙  ")
        if (coin_toss == 0):
            print("Heads")
        elif(coin_toss == 1):
            print("Tails")

coin()