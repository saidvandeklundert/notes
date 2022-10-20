import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)

# some general stats:
df.describe()
# count ocurrences:
df["gender"].value_counts()

# relative percentages:
df["gender"].value_counts(normalize=True)
# show as percentage in 100s:
df["gender"].value_counts(normalize=True) * 100

# change a value to every item in the series:
df["age"] + 100
df["age"] - 100
df["age"] / 100
df["age"] = df["age"] / 100

# get average:
df["age"].mean()
df["age"].min()
df["age"].max()
