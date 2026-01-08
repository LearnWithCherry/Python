'''
Without Enumerate!!
l = [1,2,3,4,5,6,7,8,9]
index  =  0
for item in l:
    print(f"The item number {index} is {item}")
    index += 1
'''
# this can be simplified using enumrator

# With enumerate

l = [1,2,3,4,5,6,7,8,9]
for index,item in enumerate(l):
    print(f"The item number at Index {index} is {item}")
    
# enumerate() is a built-in Python function that lets you loop through a list 
# and get the index of each item at the same time!

# Syntax = enumerate(iterable, start=0)


'''
🧠 Why use enumerate()?
✅ Cleaner code
✅ Avoids manual indexing
✅ Works with lists, tuples, strings, sets, etc.

'''