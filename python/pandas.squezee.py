import pandas as pd

import os

os.system("clear")


df = pd.DataFrame({'B':[4,5,4,5,5,1],
                   'C':[7,8,9,4,2,3],
                   'D':[1,3,5,7,1,0],
                   'E':["A5","3","6","9","2","Bb"]})

print(df)

print(df[["B"]].values.flatten())

print(pd.Series(df.values.flatten()).mode()[0])