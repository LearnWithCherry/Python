# Check if a number is an Armstrong number
n = 152
temp = n
power = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is NOT an Armstrong number")
