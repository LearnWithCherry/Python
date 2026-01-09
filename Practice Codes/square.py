# Write code below
number = int(input("Enter a number: "))
total = 0 
for i in range(1 , number+1):
  square = (i*i)
  total = total + square
print(f"Squaring {number} we get {total}")