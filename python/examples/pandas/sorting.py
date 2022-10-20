import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)


# sort df by py-score column:
df.sort_values("py-score")  # ascending is True by default
df.sort_values("py-score", ascending=False)

# sort returns a NEW dataframe unless in place is used"
df.sort_values("py-score", ascending=False, inplace=True)


# sort by 2 columns:
df.sort_values(["py-score", "name"])
df.sort_values(["py-score", "name"], ascending=[True, False])
df.sort_values(["py-score", "name"], ascending=[True, False], inplace=True)

# sort index
df.sort_index()
