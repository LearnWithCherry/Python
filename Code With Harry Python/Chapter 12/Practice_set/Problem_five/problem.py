t = int(input("Enter A number: "))

table = [t*i for i in range(1 , 11)]
with open("R://PYTHON VS CODE//12_Advance_python//Practice_set//Problem_five//Table.txt" , "a") as f:
    f.write(f"Table of {t} : {str(table)}\n")

 
