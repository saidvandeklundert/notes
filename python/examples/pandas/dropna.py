import pandas as pd
import numpy as np

df = pd.read_csv("data\movies.csv")


# add some NA values:
df["Rank"][1:10] = np.nan
df["Year"][3:5] = np.nan
df["Gross"][1:7] = np.nan
df.iloc[0] = np.nan
# Drop columns that have an NA value:
df.dropna(
    axis=0,
    how="any",
)

# Drop rows that have an NA value:
df.dropna(
    axis=1,
    how="any",
)

# Drop rows that have ALL NA value:
df.dropna(
    axis=0,
    how="all",
)
# Drop columns that have ALL NA value:
df.dropna(
    axis=1,
    how="all",
)

# rows: axis=1
# columns: axis=0
# drop rows that do not meet the threshold of at least n number of non-NA values:
df.dropna(thresh=3, axis=1)

# drop na using subset:
df.dropna(subset=["Year"], how="any")
