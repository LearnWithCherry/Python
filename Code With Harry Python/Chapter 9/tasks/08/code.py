with open("R://PYTHON VS CODE//09_file_Input_&_output//problems//08//code.txt") as f:
    content = f.read()

with open("program_of_09_problem_08.txt", "w") as f:
    f.write(content)

print("File copied successfully!")
