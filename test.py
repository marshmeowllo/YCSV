import curses
from curses import wrapper
import pandas as pd
import numpy as np
def columnWidth(array_data:list) -> int:
    maxi = []
    col_max = []
    for i in range(array_data.shape[1]):
        col_max = []
        for j in range(array_data.shape[0]):
            col_max.append(len(str(array_data[j, i])))
        maxi.append(max(col_max))
    return maxi
def optimizeWidth(array_data:list) -> list:
    maxi = []
    temp = np.transpose(array_data)
    for i in range(temp.shape[0]):
        maxi.append(max(temp[i]))
        print(i)
    return maxi
path = "airtravel.csv"
df = pd.read_csv(path, sep=',', header=None)
array_data = df.values
normal = columnWidth(array_data)
tranpose = optimizeWidth(array_data)
print(normal)
print(tranpose)

