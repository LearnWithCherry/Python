# replace all the donkey with ####

words = ["Donkey" , "the" , "of"]

with open("R:/PYTHON VS CODE/09_file_Input_&_output/problems/05/text.txt","r") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"#" * len(word))

with open("R:/PYTHON VS CODE/09_file_Input_&_output/problems/05/text.txt","w") as f:
    f.write(content)

