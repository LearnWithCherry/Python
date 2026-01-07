with open("R://PYTHON VS CODE//09_file_Input_&_output//problems//09//file1.txt") as f:
    content1 = f.read()


with open("R://PYTHON VS CODE//09_file_Input_&_output//problems//09//file2.txt") as f:
    content2 = f.read()
    
if (content1 == content2):
    print("Yes content of both the files are the same!!")
else:
    print("No content of both the files are not same!")

# a space will also show else statment!