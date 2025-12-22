
Contact_Book = {
    "Rajat" : 456789,
    "Ansh"  : 123485,
    "Kushh" : 789410
}

srch = input("Enter whose Number you want: ") 
print(f"{srch} Number is : {Contact_Book.get(srch)}")