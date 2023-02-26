import pandas as pd

# by default, Pandas will generate an index:
df = pd.read_csv("data\movies.csv")

# you can tell Pandas to use a certain column as an index:
df = pd.read_csv("data\movies.csv", index_col="Title")


# Loading it again with a wrong index:
df = pd.read_csv("data\movies.csv")
