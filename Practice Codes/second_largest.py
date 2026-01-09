numbers = [-1,-2,-3,-5,0,8]

largest = float('-inf')
second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Largest:", largest)
print("Second Largest:", second)
