import pandas as pd

df = pd.read_csv("101_py_csv_output.csv", index_col=0)

print(df)
# new column with default value
df["new-column"] = None
print(df)
