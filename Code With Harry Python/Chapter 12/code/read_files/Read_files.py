with (
    open('R://PYTHON VS CODE//12_Advance_python//Codes//read_files//file1.txt') as f1, 
    open('R://PYTHON VS CODE//12_Advance_python//Codes//read_files//file2.txt') as f2
):
    print("📄 Contents of file1.txt:")
    print(f1.read())

    print("\n📄 Contents of file2.txt:")
    print(f2.read())
