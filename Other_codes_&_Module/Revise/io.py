# file = open("X:\\VScode\\PYTHON\\Other_Programs\\Revise\\data.txt")
# data = file.read()
# # print(data)
# file.close()

# data = "Good morning."
# file = open("X:\\VScode\\PYTHON\\Other_Programs\\Revise\\data.txt", 'w')
# text = file.write(data)
# file.close()


# file = open("X:\\VScode\\PYTHON\\Other_Programs\\Revise\\data.txt", 'r')

# line = file.readline()

# while(line != ""):
#     print(line,end="")
#     line = file.readline()
# file.close()

# with open("X:\\VScode\\PYTHON\\Other_Programs\\Revise\\data.txt") as file:
    # print(file.read())                        

# with open("X:\\VScode\\PYTHON\\Other_Programs\\Revise\\data.txt") as file:
#     data = file.read()
#     if("bad" in data):
#         print("Yes it exists")
#     else:
#         print("It does not")


words = ["good","day","morning"]
with open("X:\\VScode\\PYTHON\\Other_Programs\\Revise\\data.txt" ,"r") as file:
    content = file.read()
for word in words:
    content = content.replace(word,"#&%!@")
with open("X:\\VScode\\PYTHON\\Other_Programs\\Revise\\data.txt" ,"w") as file:
    content = file.write(content)