import pandas as pd

df = pd.read_csv("101_py_csv_output.csv", index_col=0)


# rename columns:
df = df.rename(columns={"age": "AGE", "city": "CITY"})
print(df)

# rename row based on the idx using a dict:
df = df.rename(index={101: "onehundredone"})

# use mapper to rename columns:
df.rename(mapper={"age": "AGE", "city": "CITY"}, axis=1, inplace=True)
# note: the axis default is 0 (indicating rows)
