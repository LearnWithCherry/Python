a = 15 # this is a global variable
def fun():
    global a
    a = 3 #local variable
    print(a)

fun()
print(a)

'''
if global is commented out then the first a will be 15
second a is 3
but if the global is uncommented the output is both a is 3 
that means the global variable will change the a out-side the function
not inside 
'''