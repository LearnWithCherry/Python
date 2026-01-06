a = {
    "name"      :       "rajat"              ,
    "age"       :        19                  ,
    "address"   :       "Himachal pradesh"
#      key          value
}


print(a.items())
#dict_items([('name', 'rajat'), ('age', 19), ('address', 'Himachal pradesh')])

print(a.keys())
#dict_keys(['name', 'age', 'address'])

print(a.values())
# dict_values(['rajat', 19, 'Himachal pradesh'])

a.update({"nickname":"Cherry"})
print(a)
# {'name': 'rajat', 'age': 19, 'address': 'Himachal pradesh', 'nickname': 'Cherry'}

print(a.get("age"))
# 19