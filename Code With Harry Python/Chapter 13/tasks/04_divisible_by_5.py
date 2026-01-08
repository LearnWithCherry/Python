# printing number divisible by 5

def div(n):
    if(n % 5 == 0):
        return True
    return False

a = [1,2,3,4,5,6,7,8,9,10,50,100,200,500,1000]

f = list(filter(div , a))
print("Number Divisible by 5",f)
print(" ")
# printing number not divisible by 5

def div(n):
    if(n % 5 != 0):
        return True
    return False

a = [1,2,3,4,5,6,7,8,9,10,50,100,200,500,1000]

f = list(filter(div , a))
print("Number not Divisible by 5",f)