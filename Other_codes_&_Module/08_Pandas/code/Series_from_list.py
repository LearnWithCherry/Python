import pandas as pd

a = [1, 7, 2]

data = pd.Series(a)

print(data)
#           0    1
#           1    7
#           2    2
#           dtype: int64

print(data[0])
#           1