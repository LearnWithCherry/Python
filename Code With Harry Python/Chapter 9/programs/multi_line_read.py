# read function

f = open("09_file_Input_&_output\\programs\\letter to myfriend.txt","r")

line1 = f.readline()
print(line1 , end="")

line2 = f.readline()
print(line2 , end="")

line3 = f.readline()
print(line3 , end="")
print("\n")
# line5 = f.readline()
# print(line5 == "") when there is no next line function will not print any thing 
# print(type(line1)) this is used to print class or type of a string 
f.close()
