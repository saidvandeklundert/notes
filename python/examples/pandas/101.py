"""
Module with extensive functionality for working with tabular data.
"""
import pandas as pd

data = {
    "name": ["Xavier", "Ann", "Jana", "Yi", "Robin", "Amal", "Nori"],
    "city": [
        "Mexico City",
        "Toronto",
        "Prague",
        "Shanghai",
        "Manchester",
        "Cairo",
        "Osaka",
    ],
    "age": [41, 28, 33, 34, 38, 31, 37],
    "py-score": [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0],
}
index = range(101, 108)
pd_dataframe = pd.DataFrame(data, index=index)
print(pd_dataframe)
print(pd_dataframe.head(4))
print(pd_dataframe.tail(4))
# print the py-score colum:
print(pd_dataframe["py-score"])
# print the py-score colum value at location 103:
print(pd_dataframe["py-score"].loc[103])

# print values on location 103 (this is a Series object):
print(pd_dataframe.loc[103])


# create a csv:
pd_dataframe.to_csv("101_py_csv_output.csv")

# read from csv and use the first column as index:
p_df = pd.read_csv("101_py_csv_output.csv", index_col=0)

print(p_df)
p_df.index  # display the index
p_df.values  # display the values of de indexes
p_df.to_numpy()
p_df.dtypes
p_df.memory_usage()
p_df.ndim
p_df.size
p_df.shape
