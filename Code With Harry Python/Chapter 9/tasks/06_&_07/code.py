# problem 06
print("problem 06")
with open("R:/PYTHON VS CODE/09_file_Input_&_output/problems/06_&_07/log.txt" , "r")as f:
    content = f.readline()
if ("python " in content):
    print("yes")

# problem 07
print("problem 07")
with open("R:/PYTHON VS CODE/09_file_Input_&_output/problems/06_&_07/log.txt" , "r")as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes python is present! \nAt line no: {lineno}")
        break
    lineno += 1
else:
    print("No python was not there")
