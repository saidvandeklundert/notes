import pandas as pd

url = "https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip"
df = pd.read_csv(url)

cyl = df.cylinders
make = df.make
# check the missing value count:
cyl.isna().sum()


# check what is make has missing cylinders:
missing_cyl = cyl.isna()
make[missing_cyl]  # returns a series of the makes with missing cylinders.
make.loc[missing_cyl]

# fill missing values with 0:
cyl.fillna(0)

no_more_missing = cyl.fillna(0)
