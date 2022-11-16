import pandas as pd

df = pd.read_csv("data\movies.csv", index_col="Title")

# return the number of rows:
len(df)
# return a tuple: (rows, columns)
df.shape  #  (782, 4)

# return the total number of cells:
df.size

# check column data types:
df.dtypes
