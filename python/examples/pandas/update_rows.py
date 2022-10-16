"""
Module with extensive functionality for working with tabular data.
"""
import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)
df.loc[len(df)] = ["Jan", "Terheijden", 6, 99.0]
print(df)

# re-index the DF and drop the old index:
df.reset_index(drop=True)


# add another df:
df_2 = pd.read_csv("102_py_csv_output.csv", index_col=0)
df = pd.concat([df, df_2])

# add another df (legacy):
df_2 = pd.read_csv("102_py_csv_output.csv", index_col=0)
df = df.append(df_2, ignore_index=True)


df.index  # display the index
df.values  # display the values of de indexes
df.to_numpy()
df.dtypes
df.memory_usage()
df.ndim
df.size
df.shape
