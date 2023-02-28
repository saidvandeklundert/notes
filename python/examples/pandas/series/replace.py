import pandas as pd

url = "https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip"
df = pd.read_csv(url)
city_mpg = df.city08
highway_mpg = df.highway08
make = df.make

# replacing string values:
make.replace("Subaru", "SUBARU")

# replace can also contian regex:
make.replace(r"^Suba(.*)|^Do(.*)", value="CHANGED", regex=True)

# specifying all arguments in full to be more explicit:
make.replace(to_replace="Dodge", value="changed dodge")


make.replace(to_replace=r"^Suba(.*)|^Do(.*)", value="CHANGED", regex=True)

# multiple changes explicitly specified:
make.replace(to_replace={"Subaru": "SUBARU", "Dodge": "changed dodge"})
