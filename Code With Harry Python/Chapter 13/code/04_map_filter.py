from functools import reduce
#-----------------------Example of Map

from functools import reduce


l = [1,2,3,4,5,6]

square = lambda x: x*x

square_list = map(square, l)
print("After squaring all Numbers from List L: ",list(square_list))
print(" ")
#--------------------Example of Filter
# even
def even(n):
    if(n % 2 == 0):
        return True
    return False
onlyEven = filter(even , l)
print("Only Even Numbers from list L: ",list(onlyEven))
print(" ")

# odd
def odd(n):
    if(n % 2 != 0):
        return True
    return False
onlyOdd = filter(odd , l)
print("Only Odd Numbers from list L: ",list(onlyOdd))

#----------------------Reduce Function
r = [1,2,3,4,5,6,7,8,9]
def sum(a , b):
    return a + b

print(reduce(sum , r))
# how it works first it will add first two number and it will add
# 3rd number with the sum of the 1st & 2nd and so on upto nth number