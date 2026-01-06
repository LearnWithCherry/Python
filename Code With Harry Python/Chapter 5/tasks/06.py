# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 


d = {}

name = input("Enter your name: ")
langu = input("Enter language name: ")
d.update({name:langu})

name = input("Enter your name: ")
langu = input("Enter language name: ")
d.update({name:langu})

name = input("Enter your name: ")
langu = input("Enter language name: ")
d.update({name:langu})

name = input("Enter your name: ")
langu = input("Enter language name: ")
d.update({name:langu})

print(d)

# problem 6.1
# If the names of 2 friends are same; what will happen to the program in problem 6

# {'rajat': 'python', 'cherry': 'java', 'joti': 'cpp'}

# problem 6.2
# If languages of two friends are same; what will happen to the program in problem 6

# {'rajat': 'python', 'cherry': 'java', 'ruhi': 'rust', 'ruchi': 'rust'}