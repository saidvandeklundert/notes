import pandas as pd

df = pd.read_csv("https://andybek.com/pandas-drinks")

# filter by column name make sure the column is not an object
df = df["country"].astype(str)
df.filter(items=["country"])
df["country"].astype(str).filter(items="country", regex="^A")
# fitler to a column and then apply a regex to produce a boolean array
df.filter(items=["country"]).filter(regex="^A")


df[df.filter(items=["country"]).filter(regex="^A")]
