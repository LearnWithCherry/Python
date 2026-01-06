# Reverse the digits of a number
n = 1234
reverse = 0

while n > 0:
    digit = n % 10         # get last digit
    reverse = reverse * 10 + digit
    n = n // 10            # remove last digit

print("Reversed number:", reverse)
