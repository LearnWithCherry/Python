#  how to open a file 

# f = open("R:/PYTHON VS CODE/09_file_Input_&_output/codes/text.txt","r")
# text = f.read()
# print(text)
# f.close()

# methods to open a file 

# this is used to read single line 
f = open("R:/PYTHON VS CODE/09_file_Input_&_output/codes/text.txt","r")
line = f.readline()  # Read one line from the file
print(line)  # Display the line
f.close()  # Always close the file after use
# output = Hii

# this is used to read multipul lines

f = open("R:/PYTHON VS CODE/09_file_Input_&_output/codes/text.txt","r")
lines = f.readlines()  # Read one line from the file
print(lines)  # Display the line
f.close()  # Always close the file after use
# output = ['Hii \n', 'Hello how are you !\n', 'i am good\n', 'what about you']


# modes to opening a file 

# r – open for reading 

# w - open for writing  

# a - open for appending 

# +  - open for updating. 

# ‘rb’ will open for read in binary mode.

# ‘rt’ will open for read in text mode.
