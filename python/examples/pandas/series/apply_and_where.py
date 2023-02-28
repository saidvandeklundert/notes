import pandas as pd
import pandas as pd
import random

series = pd.Series([random.randint(0, 255) for _ in range(1_000_000)])


def multiply(x: int) -> int:
    return x * 2


multiplied = series.apply(multiply)

"""
The apply method applied the function to every element in the Series:
In [34]: series.iloc[0]
Out[34]: 68

In [35]: multiplied.iloc[0]
Out[35]: 136
"""

# where is used to filter a series based on a condition.
# 'where' takes a boolean array as a parameter.


# for every 'True' in the boolean array, the value from the series will be used.
# for every 'False' in the boolean array, the value from the 'other' parameter will be used.
where_applied = series.where(series.gt(100), other=10)
# in the previous, everything over 100 was kept. Everything else was replaced with 10.

# mask does the inverse of where:
mask_applied = series.mask(series.gt(100), other=10)
# in the previous, everything under 100 was kept. Everything else was replaced with 10.

"""
mask and where are about 6 times faster than apply.
"""
