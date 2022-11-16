import pandas as pd


# you can tell Pandas to use a certain column as an index:
df = pd.read_csv("data\movies.csv", index_col="Title")

df
df = df["Gross"].str.replace("$", "", regex=False).str.replace(",", "", regex=False)
df
