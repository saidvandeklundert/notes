import pandas as pd

url = "https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip"
df = pd.read_csv("vehicles.csv.zip")
city_mpg = df.city08
highway_mpg = df.highway08
make = df.make

# rename the index of city by doing a lookup in the dict gotten by transforming the
# make series into a dict:
city_2 = city_mpg.rename(make.to_dict())
# result is prev idx is not the value of the make column of that row
city_2.index


# we can also renam the idx of a series by passing in a series:
city_3 = city_mpg.rename(make)

# to change the name of the series:
city_2 = city_2.rename("city_2_series")

# outfit a series with a unique monotonic increasing index:
city_2.reset_index()

# while droppg current index
city_2.reset_index(drop=True)

# use loc and reference a label to pull info from the series:
city_2.loc["Subaru"]
"""
loc can take a:
- scalar value (like above)
- a list of index labels
- a slice of index labels
- an index
- a boolena array
- a function that accepts a series and returns one of the above
"""
# slice using labels:
city_2.sort_index().loc["Ferrari":"Subaru"]

# no need to specify full label:
city_2.sort_index().loc["F":"T"]

# using a boolean array will return values where the idx for the series evaluates
# to True:
mask = city_2 > 50
city_2.loc[mask]
# duplicate labels will return a series, unique labels will return just the value
city_2["Fisker"]
"""
>>> 20
"""
# to ensure you get a series returned, pass in a list:
city_2[["Fisker"]]
"""
Fisker    20
Name: city_2_series, dtype: int64
"""

"""
iloc can take a :
- scalar integer as idx position
- list of idx positions
- slice
- numpy array or Python list of boolean values
- function that accepts a series and returns one of the above
"""
city_2.iloc[1]
city_2.iloc[2:100]
city_2.iloc[2:]
# to ensure you get a series returned, pass in a list:
type(city_2.iloc[0])  # numpy.int64
type(city_2.iloc[[0]])  # pandas.core.series.Series

# we can also use a boolean numpy array or python list.
# pandas boolean will fail:
city_2.iloc[city_2 > 50]
# just convert it first:
pandas_bool_arr = city_2 > 50
city_2.iloc[pandas_bool_arr.to_numpy()]
# or
city_2.iloc[list(city_2 > 50)]


# quick insights:
city_2.head(4)
city_2.tail(4)

# series might be sorted giving false impressions using head or tail,
# use sample:
city_2.sample(
    10,
)
city_2.sample(10, random_state=42)


"""
We can filter by exavt match, substring or regex.

The mutually exclusive oeprators are:
- items
- like
- regex parameters

Exact match using items will fail if there are duplicate labels
"""
# item filter:
city_2.filter(items=["Ford", "Subaru"])
# substring filter:
city_2.filter(like="rd")
# regex:
city_2.filter(regex="(Ford)|(Subaru)")

# re-index can pull out values even though the idx does not exist.

# does not work when there are duplicate idx values
city_2.reindex(["missing", "Ford"])

# does not matter if you inster the same idx multiple times:
city_mpg.reindex([0, 0, 10, 20, 2_000_000_000])

"""
Re-index can be super helpful if you have series that have portions of idx lables
that are the same and you want to have the index of the other
"""

s1 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
s2 = pd.Series([15, 25, 35], index=["b", "c", "d"])
s2.reindex(s1.index)
