myList = [1,2,3,4,5,6,9,10]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)


squaredList = [i*i for i in  myList] # square all number from the list
print("Squaring all Numbers\n",squaredList)
squaredEvens = [i*i for i in myList if i % 2 == 0] #square only even numbers
print("Squaring Only Even Numbers\n",squaredEvens)