import pandas as pd

df = pd.read_csv("101_py_csv_output.csv")

# iterate the labels
for i in df:
    print(i)


for i in df.index:
    print(i)
    print(df.iloc[i])


# lazyily evaluated, everything as a tuple
for i in df.items():
    print(type(i))
    print(dir(i))
