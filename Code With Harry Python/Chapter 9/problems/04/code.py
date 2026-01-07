# replace all the donkey with ####

word = "Donkey" 

with open("R:/PYTHON VS CODE/09_file_Input_&_output/problems/04/donkey.txt","r") as f:
    content = f.read()

contentnew = content.replace(word , "######")

with open("R:/PYTHON VS CODE/09_file_Input_&_output/problems/04/donkey.txt","w") as f:
    content = f.write(contentnew)

