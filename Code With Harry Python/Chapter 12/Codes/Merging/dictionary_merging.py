dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c': 4} 

merged = dict1 | dict2 
print(merged)


'''
" | " is the dictionary merge operator

It merges two dictionaries together, 
creating a new one.

If a key exists in both dictionaries ('b' in this case),
then the value from the right dictionary (dict2) wins.
'''