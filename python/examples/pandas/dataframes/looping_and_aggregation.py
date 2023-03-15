import pandas as pd
import numpy as np
from similarities_df_series import tweak_siena_pres

df = pd.read_csv("siena2018-pres.csv", index_col=0)

# for looping over the DF is possible but not recommended as it is not
# a vectorized operation and it will be a lot slower.


for column_name, column in df.iteritems():
    print(column_name, type(column))
    print(column)


# iterrows gives the column name and the row as a series:
for idx, row in df.iterrows():
    print(idx, type(row))
    print(row)

# iterates over the rows as named Tuples:
for tup in df.itertuples():
    print(tup.President, tup.Party)


# aggregating:
# isolate the columns using .loc, then sum along the columns
# and divide the result by the lenght of the columns:
pres = tweak_siena_pres(df)
scores = pres.loc[:, "Bg":"Average_rank"]
scores.sum(axis="columns") / len(scores.columns)

# the agg methods according to the docs:
#  Aggregate using one or more operations over the specified axis.
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html
ex_df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [np.nan, np.nan, np.nan]], columns=["A", "B", "C"]
)
ex_df.agg(["sum", "min"])

pres.agg({"Luck": ["count", "size"], "Overall": ["count", "max"]})
"""
Out[15]: 
       Luck Overall
count  44.0      44
size   44.0     NaN
max     NaN      44
"""

# meta-aggregation with summary statistics for each numeric column:
pres.describe()
