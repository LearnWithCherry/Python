import pandas#-------------->This line imports the pandas library into your Python program.
# import pandas as pd you can also write like ths
mydataset = { #-------------->This is a Python dictionary with two keys:
  'cars': ["BMW", "Volvo", "Ford", "KIA", "Audi", "Hundai"],
  'passings': [3, 7, 2, 5, 6, 9]
}

Data = pandas.DataFrame(mydataset)#-------------->You are converting the dictionary into a DataFrame
Data.at[2, "cars"] = "Koniseeg"#-------------->to change value 
print(Data.head())#-------------->This prints the table-like structure
print(Data)#-------------->This prints first 5 rows
print(Data["cars"])#-------------->for specific dat

