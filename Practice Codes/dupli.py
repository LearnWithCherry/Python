oldlist = [1,2,2,3,4,5,5,6]

newlist = []
for num in oldlist:
    if num not in newlist:
        newlist.append(num) 


print(newlist)


