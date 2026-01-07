f = open("R://PYTHON VS CODE//09_file_Input_&_output//problems//1//01.txt","r")
text = f.read()
print(text)

if("stars" in  text):
    print("yes")

else:
    print("no")
f.close()