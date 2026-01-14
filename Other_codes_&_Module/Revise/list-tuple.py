# list can be changes(mutable)

friends = ["Apple","Orange",5,3.454,False]
# print(friends)

# print(friends[0])
friends[0] = "BMW"
# print(friends)

# print(friends[1:4]) # go upto 4 but do not include = ['Orange', 5, 3.454]

# list methods

data = ["Rajat","Bhardwaj","Student","LPU"]

data.append("CSE") # add at the end

data.remove("CSE") # Remove selected

data.insert(1,"Good") # insert at given index

data.pop(1) #remove at given index

value = data.pop(1)
# print(value)
# print(data )
# number = [1,0,8,7,5,3,10] 
# number.sort() # list wil be sorted
# number.reverse()# list wil be reversed
# print(number)

# learn more method of list 

# ----------------------------------------
# tuple - immutable

a = ("Rajat",3.2,1)

# print(type(a))
c = a.count(1) 
print(c)

# practice problems

# q1 = []

# total = int(input("Enter total fruit count: "))
# i = 0
# while(i<total):
#     friut = input("Enter Fruit name: ")
#     q1.append(friut)
#     i = i + 1

# print(q1)


# q3 = []

# total = int(input("Enter total Student count: "))
# i = 0
# while(i<total):
#     marks = int(input("Enter Student marks: "))
#     q3.append(marks)
#     i = i + 1
# q3.sort()
# print(q3)



total = [1,2,3,4,5]
print(sum(total))


total = (1,0,2,0,3,4,0,5)
totalzero = total.count(0)
print(totalzero)
