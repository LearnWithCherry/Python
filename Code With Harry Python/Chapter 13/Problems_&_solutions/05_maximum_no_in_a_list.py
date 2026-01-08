from functools import reduce

a = [2,3,4,5,6,7,8,9,10,50,100,200,1,500,1000]

def greater(a ,b):
    if(a > b):
        return a
    return b
print(reduce(greater , a))

def smaller(a , b ):
    if(a < b):
        return a
    return b
print(reduce(smaller , a))