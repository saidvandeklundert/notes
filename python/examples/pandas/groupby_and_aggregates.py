"""
Pandas groupby and aggregates explanations:

A groupby operation involves some combination of splitting the object, applying a function, and combining the results.
 This can be used to group large amounts of data and compute operations on these groups.

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.groupby.html

"""
import pandas as pd
import numpy as np

df = pd.read_csv("data\games_sales.csv")

## SIMPLE AGGREGATIONS:

# all rows of a few columns summed, vertical aggregation:
df.loc[:, ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()
df.loc[:, ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].std()
df.loc[:, ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].median()

# horizontal aggregation is done by changing the axis:
df.loc[:, ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum(axis=1)


## Conditional aggregates:
# find sales for X360 and PS3
df.Platform.unique()  # array(['X360', 'PS3', 'PS4', 'XOne'], dtype=object)
sales = df.loc[:, ["Platform", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]]

sales.sum()  # all sales
sales.sum(numeric_only=True)  # all sales, but only numeric columns

# sales for X360:
sales.loc[sales.Platform == "X360"].sum(numeric_only=True)

# using groupby:
# split the groups by platform,
#  then sum the numeric columns for every group:
sales.groupby("Platform").sum(numeric_only=True)
# this is also known as the split-apply-combine pattern

# lazy evaluation of groupby:
sales.groupby("Platform")
# equivalent to:
sales.groupby(sales["Platform"])

# as soon as we apply a method on the groupby object, the split-apply-combine pattern is applied:

# customize index to group mappings:
platform_names = {
    "XOne": "XBOX",
    "X360": "XBOX",
    "PS3": "Playstation",
    "PS4": "Playstation",
}
# Projection from one label to another only works on the index column:
sales.set_index("Platform").groupby(platform_names).sum(numeric_only=True)


# extract series from the dataframe:
ser = df.loc[:, ["Genre", "Global_Sales"]].set_index("Genre").squeeze()
# ser has Genre as index and Global_Sales as values
ser.groupby("Genre").mean()
ser.groupby("Genre").mean().sort_values(ascending=False)

# Iterate groups:
sales.Platform.unique()
for i in sales.groupby("Platform"):
    print(type(i))
    print(i)

for name, df in sales.groupby("Platform"):
    print(50 * "-")
    print(name)
    print(50 * "-")
    print(df)

# we can use grouby and iter to create a dictionary of dataframes:
d = dict(iter(sales.groupby("Platform")))
d.keys()  # dict_keys(['PS3', 'PS4', 'X360', 'XOne'])

# better is:
sales.groupby("Platform").get_group("PS3")

# multi-index grouping:
df = pd.read_csv("data\games_sales.csv")
studios = df.loc[:, ["Genre", "Publisher", "Global_Sales"]]

# top publiser by global sales:
studios.groupby(["Publisher"]).sum().sort_values(by="Global_Sales", ascending=False)

# top publisher by global sales for each genre:
studios.groupby(["Genre", "Publisher"]).sum().sort_values(
    by="Global_Sales", ascending=False
)
# order does not seem to matter:
studios.groupby(["Publisher", "Genre"]).sum().sort_values(
    by="Global_Sales", ascending=False
)


# using aggregate:
studios.groupby(["Publisher", "Genre"]).aggregate("sum")
studios.groupby(["Publisher", "Genre"]).agg("sum")

# aggregate can accept multiple functions:
studios.groupby(["Publisher", "Genre"]).agg(["sum", "mean", "count", "std"])
