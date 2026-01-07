'''
Write a Class 'Train' which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. 
'''

import random 

class train():

    def __init__(slf , trainNo , seatNo , location ,Price):
        slf.trainNo = trainNo
        slf.seatNo = seatNo
        slf.location = location
        slf.price = Price
    def train(slf):
        print(f"Your train NO is {slf.trainNo} \nAnd the seat number is {slf.seatNo}")
    def loc(self):
        print(f"Train is coming from {self.location}")
    def pri(self):
        print(f"Price of the seat is {random.randint(500 , 3500)}")
        

t = train(44589 , "32A" , "Chandighar and going to Mumabi" , "")
t.train()
t.loc()
t.pri()


# yes and you can change the self parameter to slf and it will still prints