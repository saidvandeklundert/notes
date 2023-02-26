import pandas as pd

url = "https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip"
df = pd.read_csv(url)
city_mpg = df.city08
highway_mpg = df.highway08


# sort in ascending order have have the index value stick to the values as they are sorted:
city_mpg.sort_values()

city_mpg[34563]
city_mpg.sort_values()[34563]

sorted_city_mpg = city_mpg.sort_values()

sorted_city_mpg[34563]

sorted_city_mpg[34563] == city_mpg[34563]  # True
sorted_city_mpg[34] == city_mpg[34]  # True
for i in range(len(sorted_city_mpg)):
    print(sorted_city_mpg[i] == city_mpg[i])  # True


# we can also sort the index values:
sorted_city_mpg.sort_index()
