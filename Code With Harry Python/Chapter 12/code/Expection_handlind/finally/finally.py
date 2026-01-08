try:
    f = open("12_Advance_python//Codes//Expection_handlind//finally//hello.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found 🚫")
finally:
    print("Closing file... ✅")
