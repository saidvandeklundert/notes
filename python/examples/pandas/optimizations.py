import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)

# check Nan values, total columns/rows and memory usage:
df.info()

# convert floats to integers to reduce memory:
df["py-score"] = df["py-score"].astype(int)
df.info()

# or in place:
df = df["py-score"].astype(int)


# columns with a large number of entries that have very little
# variations. For example: sex: male/female.

# identify unique values:
df.nunique()
# memory usage: 480.0+ bytes
df["gender"] = df["gender"].astype("category")
df.info()  # with very small values, categories uses more
# use a faster engine for loading csv data:
df = pd.read_csv(
    "101_py_csv_output.csv",
    engine="pyarrow",
)
