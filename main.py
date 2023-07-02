# import pandas as pd
import pandas as pd

# simple array
data = [1, 2, 3, 4]

ser = pd.Series(data)
print(ser)

print(ser.dtype)

# custom index
Sub = ['Math', 'Geo', 'Hist', 'Hindi']
Marks = [19, 20, 20, 40]

a = pd.Series(Marks, index=Sub, name='Anirudha')
print(a)

# Pandas Dictionary

dic1 = {
    'Math': 20,
    'Geo': 30,
    'Hindi': 10
}
print(pd.Series(dic1))
