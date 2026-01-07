
for i in range(0, 21):
    file_path = f"R:\\PYTHON VS CODE\\09_file_Input_&_output\\problems\\03\\tables\\table_of_{i}.txt"
    f = open(file_path, "w")
    f.write(f"Multiplication Table of {i}\n")
    f.write("=" * 25 + "\n")
    for j in range(1, 11):
        line = f"{i} x {j} = {i * j}\n"
        f.write(line)
    f.close()

print("All tables from 0 to 20 are created successfully in your folder!")

# explatation 

'''
This for loop repeats from 2 to 20 (including 20). first line


'''