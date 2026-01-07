
f = open("09_file_Input_&_output\\programs\\letter to myfriend.txt", "r")

line = f.readline()

while line != "":
    print(line, end='')  # use end='' to avoid extra newlines
    line = f.readline()

f.close()
