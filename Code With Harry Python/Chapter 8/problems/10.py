# print prime number
# prime number are those who cancellled only by then self or by one !!!!


def prime(n):
    if n < 2:
        return False
    for i in range(2 , int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for num in range(1 , 101):
    if prime(num):
        print(num , end=",")
