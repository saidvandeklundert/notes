import pandas as pd

# Nan is None
df = pd.read_csv("https://andybek.com/pandas-drinks")

df.isnull()
all_null = df[df["beer_servings"].isnull()]
non_null = df[~df["beer_servings"].isnull()]

# alternative
df["beer_servings"].notnull()
df["beer_servings"].notna()

# get the number of null elements:
df["beer_servings"].isnull().sum()

# drop null
df["beer_servings"].dropna()
df["beer_servings"].dropna(inplace=False)

# fill null
df["beer_servings"].fillna(0)
