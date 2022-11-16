import pandas as pd

# by default, Pandas will generate an index:
pd.read_csv("data\movies.csv")

# you can tell Pandas to use a certain column as an index:
pd.read_csv("data\movies.csv", index_col="Title")
