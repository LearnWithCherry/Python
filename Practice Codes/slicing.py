l = "abcdefghijk"

print(l[0:11])

# a,b,c,d,e,f,g,h,i,j,k 
# 0,1,2,3,4,5,6,7,8,9,10
# so if i write 11 it means it will go
# upto 10 index because it stats with 0 not 1
# if i have to print all characters i have write 
# n number not index number

print(l[::])
# to print whole list

print(l[::2])
# acegik will jump to n character

print(l[2:8:2]) 
# start:stop:step 
# start at index 2 go upto index 8 and jump index 2 upto index 8

print(l[::-1])
# reverse string = kjihgfedcba