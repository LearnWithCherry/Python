s1 = {1,2,3,4,5,6,7}
s2 = {1,2,6,5,4,7,9,5,5}

print(s1.union(s2))
# will return all the non duplicated numbers = {1, 2, 3, 4, 5, 6, 7, 9}

print(s1.intersection(s2))
# will only return interger who are present in both the sets = {1, 2, 4, 5, 6, 7}
