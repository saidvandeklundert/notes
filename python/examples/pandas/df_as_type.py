import pandas as pd
import numpy as np

# by default, Pandas will generate an index:
df = pd.read_csv("data\movies.csv")


# to check the types in the frame:
df.info()

# we have int64 and object types


# convert column to a different type:
df["Rank"].astype(float)

# convert column to a different type using dict:
new_df = df.astype({"Rank": float, "Year": str})

new_df.info()  # displays the new types
new_df = df.astype({"Rank": np.int16, "Year": np.int16})
