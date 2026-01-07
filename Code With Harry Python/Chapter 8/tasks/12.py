def magic(x):
    if x == 0:
        return 1
    else:
        return x * magic(x - 1)

print(magic(4))
# Think! This is recursion!
# 24 : (4x3x2x1)