num = int(input("Enter a number that you want to check: ")) 
numLen = len(str(num))
sum = 0 
temp = num

while(temp > 0):
    digit = temp % 10
    sum += digit ** numLen
    temp //= 10

if sum == num:
    print("It is a Armstrong Number.")
else:
    print("it is not a Armstrong number.")