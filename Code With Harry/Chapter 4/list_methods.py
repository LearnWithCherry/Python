friends = ["Apple" , 1545 , 22.2255 , "Rajat" , True ]
#             0        1       2         3        4
print(friends[1])

friends.append("Cherry")
print(friends)
# append adds new characters in the list

l2 = [1,8,9,5,47,998,2,4,5,6,9,7,]
l2.sort()
print(l2)
# arrange the list in assending order

l2.reverse()
print(l2)
# reverse the order of the list 

l3 = [1,2,4,5,6,9,7,4,6,2,3,3]
l3.insert(1      ,     69)   
#         index       number
print(l3)
# insert the give number at the choosen index 

l3.pop(7)
print(l3)
#  Will delete element at index

l3.remove(9)
print(l3)
#  Will remove 9 from the list.