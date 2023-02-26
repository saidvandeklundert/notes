"""
Module with extensive functionality for working with tabular data.
"""
import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)

# return a new df without the city column:
df.drop(columns=["city"])

# return a new df without city and age:
df.drop(columns=["city", "age"])

# delete city and age in current df and return 'None':
df.drop(columns=["city", "age"], inplace=True)
