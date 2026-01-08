'''
try:
    # risky code
except SomeError:
    # handle that error
else:
    # runs if no error happens
finally:
    # always runs (like cleanup)
'''

# commen types of expection

'''
🔥 Common Exceptions:
Error	                    Why It Happens
ZeroDivisionError	        Divide by zero
ValueError	                Wrong value type (e.g. int("hi"))
TypeError	                Mismatched types ("hi" + 5)
FileNotFoundError	        file doesn’t exist
IndexError	                List index out of range
KeyError	                Dictionary key not found
'''