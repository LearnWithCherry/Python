'''
Write a Class 'Train' which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. 
'''

import random 

class train():

    def __init__(self , trainNo , seatNo , location ,Price):
        self.trainNo = trainNo
        self.seatNo = seatNo
        self.location = location
        self.price = Price
    def train(self):
        print(f"Your train NO is {self.trainNo} \nAnd the seat number is {self.seatNo}")
    def loc(self):
        print(f"Train is coming from {self.location}")
    def pri(self):
        print(f"Price of the seat is {random.randint(500 , 3500)}")
        

t = train(44589 , "32A" , "Chandighar and going to Mumabi" , "")
t.train()
t.loc()
t.pri()