import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)


df.to_dict()
