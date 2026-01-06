# # problem 7.1
# # Stars pattern!

# '''
#    *
#   ***
#  *****
# *******

# '''
# # n = int(input("Enter how many star line you want: "))
n = 3
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print(" ")

# # problem 7.2
# '''
# #
# ##
# ### 
# '''
n = 3
for i in range(1,n+1):
    print("#" * i,end="")
    print(" ")

# problem 7.3
# * * * 
# *   *   for n = 3 
# * * *  
n = 5
for i in range(1,n+1):
    if(i == 1 or i == n):
        print("* "*n,end="")
    else:
        print("*", end="")
        print(" "*(n+2), end="")
        print("*", end="")
    print(" ")