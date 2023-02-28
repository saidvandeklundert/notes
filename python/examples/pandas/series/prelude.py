import pandas as pd

url = "https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip"
df = pd.read_csv("vehicles.csv.zip")
city_mpg = df.city08
highway_mpg = df.highway08
make = df.make
