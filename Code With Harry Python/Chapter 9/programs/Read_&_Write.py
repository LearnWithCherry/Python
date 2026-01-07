# read function
f = open("R:/PYTHON VS CODE/09_file_Input_&_output/codes/text.txt","r")
lines = f.readlines()
print(lines)
f.close()

# write function

letter = "Hey \n how are you \n long time no see"

f = open("R:\\PYTHON VS CODE\\09_file_Input_&_output\\programs\\letter to myfriend.txt", "w")

f.write(letter)

f.close()

# use \\ when you are writing into a file