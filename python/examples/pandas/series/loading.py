import pandas as pd

url = "https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip"
df = pd.read_csv(url)
city_mpg = df.city08
highway_mpg = df.highway08
type(highway_mpg)
"""
>>> pandas.core.series.Series
"""

highway_mpg_list = highway_mpg.to_list()
from pympler.asizeof import asizeof

asizeof(highway_mpg_list)
highway_mpg.memory_usage()
