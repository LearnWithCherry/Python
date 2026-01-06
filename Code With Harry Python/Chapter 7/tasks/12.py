# find all the odd/even numbers from 1 to 100
def odd():
    for i in range(2 , 101):
        if(i % 2 != 0) :
            print(f"Its an prime Number = {i} !!")
    print("Thank you") 

odd()


def even():
    for i in range(1 , 101):
        if(i % 2 == 0 ):
            print(f"This number is Even Number = {i}")
    print("Thank you")
even()
