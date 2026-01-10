tup = (1,2,3,4,5,6,7)
lar = tup[0]

for num in tup:
    if num > lar:
        lar = num

print(lar)