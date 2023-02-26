import pandas as pd

url = "https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip"
df = pd.read_csv(url)
city_mpg = df.city08
highway_mpg = df.highway08

"""
Drop duplicates:
"""
city_mpg.drop_duplicates()


"""
Default is to keep the first duplicate value. You can also change this:
"""

city_mpg.drop_duplicates(keep="last")
