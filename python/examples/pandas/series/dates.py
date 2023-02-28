import pandas as pd

dates_list = [
    "2015 -03 -08 08:00:00+00:00 ",
    "2015-03-08 08:30:00+00:00 ",
    "2015-03-08 09:00:00+00:00 ",
    "2015-03-08 09:30:00+00:00 ",
    "2015-11-01 06:30:00+00:00 ",
    "2015-11-01 07:00:00+00:00 ",
    "2015-11-01 07:30:00+00:00 ",
    "2015-11-01 08:00:00+00:00 ",
    "2015-11-01 08:30:00+00:00 ",
    "2015-11-01 08:00:00+00:00 ",
    "2015-11-01 08:30:00+00:00 ",
    "2015-11-01 09:00:00+00:00 ",
    "2015-11-01 09:30:00+00:00 ",
    "2015-11-01 10:00:00+00:00 ",
]

# record dates:
col = pd.Series(dates_list)

# convert to UTC:
utc_s = pd.to_datetime(col, utc=True)
utc_s
# now it is of the dtype datetime64[ns, UTC]

# once converted to datetime, you can use the 'dt' accessor:
utc_s.dt.tz_convert("America/Denver")
utc_s.dt.tz_convert("Europe/Paris")
ams_time = utc_s.dt.tz_convert("Europe/Amsterdam")
utc_s.dt.tz_convert("America/Denver")
# convert to UTC
utc_s.iloc[0] = "1970-01-01 00:00:01+00:00"
utc_s.dt.tz_convert("UTC")
epoch = utc_s.view("int64").floordiv(1e9).astype(int)
epoch

alta_df = pd.read_csv("alta-noaa-1980-2019.csv")
dates = pd.to_datetime(alta_df.DATE)

snow = alta_df.SNOW.rename(dates)

snow
snow.loc["1987 -12-30":"1988-01-10"]
