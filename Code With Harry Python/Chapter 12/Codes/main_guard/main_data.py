def data():
    print("Hi \nMy name is Rajat")

if __name__ == "__main__":
    print("We are directly Running this code!")
    data()
    print(__name__)


# When you run a Python file directly, Python sets a special variable called __name__ to "__main__".

# So, this line:

# if __name__ == "__main__":
# means:

# 👉 “Run this part only if this file is being run directly, not imported.”
# if this code is directly executed by running the file its present in
# -------------------------------------------


# if i run this code here i will get

'''
Hi 
My name is Rajat
__main__
'''

# but if i run this code in other file like in main.py
# then the output will be different

'''
Hi 
My name is Rajat
main_data
'''
# print(__name__) this module will print the name of that file in which it is imported from 

# here the output is __main__ because this file is imported in main.py