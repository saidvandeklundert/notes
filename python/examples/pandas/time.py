import pandas as pd
import numpy as np

# times
time = pd.Timestamp(
    "2023-02-01T16:06:48Z",
)
# make it unambiguous:
time = pd.to_datetime("2023-02-01T16:06:48Z", dayfirst=True, utc=True)
# 30 days ago:
now = pd.to_datetime("now", dayfirst=True, utc=True)
thirty_days_ago = now - pd.Timedelta("30 days")
# is time within 30 days of now?
thirty_days_ago < time  # True
thirty_days_ago < (now - pd.Timedelta("40 days"))  # False
thirty_days_ago < (now - pd.Timedelta("10 days"))  # True

# read frame:
brent = pd.read_csv("data\BrentOilPrices.csv")
brent.head()
brent.info()
brent.dtypes

brent.info(memory_usage="deep")
brent.Date = brent.Date.astype(np.datetime64)
brent.dtypes
brent.info(memory_usage="deep")

brent.set_index("Date", inplace=True)


# read the frame with the data as index and parse the dates:
brent = pd.read_csv("data\BrentOilPrices.csv", index_col=0, parse_dates=True)
brent.dtypes  # index is datetime64[ns] even though it says object
brent.info(memory_usage="deep")

# select a date or a range of dates:
brent.loc["2017-01-03"]
brent.loc["2017-01-03":"2017-01-31"]
# partial:
brent.loc["2019-01"]

# first two monthts of 2019:
brent.loc["2019-01":"2019-02"]
# up untill 2019-02:
brent.loc[:"2019-02"]

# up untill thirty days ago:
thirty_days_ago = now - pd.Timedelta("30 days")
brent.loc[:thirty_days_ago]
