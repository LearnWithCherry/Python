def remove(l, word):
    if word in l:
        l.remove(word)
    return l

l = ["Rajat" , "cherry" , "yes"]

print(remove(l , "yes"))


def remove(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n 
l = ["Rajat" , "cherry" , "hold"]

print(remove(l , "hold"))
