import pandas as pd

# by default, Pandas will generate an index:
df = pd.read_csv("data\movies.csv")
# rows and colums
df.axes

# list of rows:
df.axes[0]

# list of columns:
df.axes[1]
# item 2 in the column:
df.axes[1][2]


# drop columns with missing values:
df.dropna(axis=0)
# drop rows with missing values:
df.dropna(axis=1)
