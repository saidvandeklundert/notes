import pandas as pd
import numpy as np

d = {"x": [1, 2, 3], "y": np.array([2, 4, 8]), "z": 100}
# create a dataframe
df = pd.DataFrame(d, index=[100, 200, 300], columns=["z", "y", "x"])
print(df)


lst = [
    {"x": 1, "y": 2, "z": 100},
    {"x": 2, "y": 4, "z": 100},
    {"x": 3, "y": 8, "z": 100},
]
df = pd.DataFrame(lst)
print(df)

lst2 = [[1, 2, 100], [2, 4, 100], [3, 8, 100]]
arr = np.array([[1, 2, 100], [2, 4, 100], [3, 8, 100]])
df = pd.DataFrame(arr, columns=["x", "y", "z"], copy=True)  # pass by value
print(df)
