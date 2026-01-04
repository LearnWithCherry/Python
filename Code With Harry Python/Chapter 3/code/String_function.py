name = "rajat"

print(len(name))
# this will count length of the string
print(name.endswith("jat"))
# this will verify that the string ends with entered string
count = name.count("a")
print(count)
# this counts how many letter are there is the string
capitalized_string = name.capitalize()
print(capitalized_string)
# this will capatize the string first characters
index = name.find("t") 
print(index)
# find the index of first occurrence of that word in the string 
replaced_string = name.replace("rajat" , 'cherry')
print(replaced_string)
# it will replace the old string and give a new string 