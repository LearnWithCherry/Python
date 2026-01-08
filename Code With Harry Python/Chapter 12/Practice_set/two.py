# print 3,5 and 7 content of the list 

l = [1,2,3,4,5,6,7,8,9]

for num,item in enumerate(l):
    if num == 2 or num == 4 or num == 6:
        print(item)