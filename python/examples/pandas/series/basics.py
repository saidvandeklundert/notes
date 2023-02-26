"""
There is another advantage to broadcasting. With many math operations, these are optimized
and happen very quickly in the CPU. This is called vectorization. (A numeric pandas series is a
block of memory, and modern CPUs leverage a technology called Single Instruction/Multiple Data
(SIMD) to apply a math operation to the block of memory.)
"""
import pandas as pd

# create 2 series:
s1 = pd.Series([10, 20, 30], index=[1, 2, 2])
s2 = pd.Series([35, 44, 53, 1213], index=[2, 2, 4, 4], name="s2 ")

# fill s1 to match s2:
s1 = s1.reset_index(drop=True)
s2 = s2.reset_index(drop=True)
s1.add(s2, fill_value=0)


# you can also use operators to add, but methods are preferred since
# that makes chaining easier:
url = "https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip"
df = pd.read_csv(url)
city_mpg = df.city08
highway_mpg = df.highway08
city_mpg.add(highway_mpg).div(2)


"""


"""
# some usefull methods and attributes:
city_mpg.mean()
city_mpg.is_unique
city_mpg.is_monotonic
city_mpg.quantile()  # 50% by default

# counting the sum of values that meet a criteria:
city_mpg.gt(20).sum()
city_mpg.gt(20).mul(100).mean()


# aggregates:
import numpy as np


def second_to_last(s: pd.Series) -> pd.Series:
    """Return the second to last item in a series"""
    return s.iloc[-2]


# https://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html
city_mpg.agg("mean")
city_mpg.agg([second_to_last])
city_mpg.agg(["mean", np.var, max, second_to_last])


city_mpg.notna().sum()
city_mpg.count()  # or len(city_mpg)
len(city_mpg.unique())  # number of unique values
city_mpg.mean()  # get the mean
city_mpg.max()  # get the max


def sum_notna(s: pd.Series) -> pd.Series:

    return s.notna().sum()


city_mpg.agg(["sum_notna"])
