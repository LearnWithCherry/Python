'''Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
present, a message without exiting the program must be printed prompting the same.'''

# Method for checking large number of files

files = ["file1.txt", "file2.txt", "file3.txt"]#----------------------------------------help to loop 
base_path = "R://PYTHON VS CODE//12_Advance_python//Practice_set//Problem_ONE//"#-------all the files are stored in the same path
                                                                                #-------instead of repeating path again and again you just write it one c

for filename in files:#-----------------------------------------------------------------this loops thought each filename one by one
    try:#-------------------------------------------------------------------------------open file if dosen't exist code jumps to the expect block instead of crashing
        with open(base_path + filename, 'r') as f:#-------------------------------------this line tries to open the file using given path and opened in read mode
            print(f"\n📂 Printing content of {filename}...")
            print(f.read())#------------------------------------------------------------if the file of found, it will print its content 
    except FileNotFoundError:#----------------------------------------------------------if the file is missing thiis runns instead of crashing & prints file not found
        print(f"❌ {filename} not found!")
    except Exception as e:#-------------------------------------------------------------catches any other error
        print(f"⚠️ Some other error occurred with {filename}: {e}")

print("\n✅ All file attempts done. Program did not crash.")#---------------------------this will print in the end after every block is runned and thi will confirm that code run with crashing 
