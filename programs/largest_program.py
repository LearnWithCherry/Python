import random
num1 = random.randint(1,200)
num2 = random.randint(1,200)
num3 = random.randint(1,200)
if(num1 < num2 < num3):
    print(f"The largest number is Number 1 which is: {num1}..")
elif(num1 < num3 < num2):
    print(f"The largest number is Number 2 which is: {num2}..")
else:
    print(f"The largest number is Number 3 which is: {num3}..")

# this with loop 
numbers = [1000, 200, 30]  
largest = numbers[0]        
for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is {largest}..")
