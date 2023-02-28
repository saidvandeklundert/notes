import pandas as pd
from .prelude import make, city_mpg, df, highway_mpg

# string is of the type object by default
make.info()
# since pandas 1.0, you can interpret object as a string:
make.astype("string")

"""
The main difference between the 'string' type and strings stored in object (and category) type
series is that the string methods return the nullable type when you use a 'string' series. If the
result of the string method is missing, pandas will use the newer types that have native pandas
nullable types. Otherwise, the behavior is similar.
"""


# convert to category in order to save memort:
make.astype("category")


# object, string and category types have the str accessor
# using this accessor, you have access to string manipulation methods
# that are modeled after the ones found in Python
make.str.lower()
make.str.startswith("Su")
make.str.lower().str.startswith("su")
make.str.find("u")

# extract using regex
make.str.extract(r"([^a-z A-Z])")
make.str.extract(r"([^a-z A-Z])", expand=False).value_counts()

make.str.extract(r"(Su.*)")
make.str.extract(r"(Suz.*)").value_counts()

# splitting
make.str.split()
make.str.split("r")

# replacing
make.str.replace("Subaru", "Yolo")

# replace multiple things:
make.replace({"Dodge": "new-Dodge", "Subaru": "new-subaru"})

# replace using regex:
make.replace("u", "a", regex=True)
