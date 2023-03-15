"""
Dataframes are best understood when thought of as columnar, where every
column is a pandas Series.

Axis 0: the rows
Axis 1: the columns
"""
import pandas as pd


# create a Dataframe that has 2 columns and 4 rows:
df = pd.DataFrame(
    {"growth": [0.5, 0.7, 1.2, 1.4], "Name": ["Paul", "George", "Ringo", "Starr"]}
)

# accessing a row by index:
df.iloc[0]
# accessing a column:
df["Name"]
df.Name

# a column is a series:
type(df["Name"])

"""
The DataFrame overrides __getattr__ to allow access to columns as attributes. This tends to work
ok, but will fail if the column name conflicts with an existing method or attribute. It will also
fail if the column has a non-valid attribute name (such as a column name with a space)
"""

# the previous DF could have also been created from rows:
df = pd.DataFrame(
    [
        {"growth ": 0.5, "Name ": "Paul "},
        {"growth ": 0.7, "Name ": "George "},
        {"growth ": 1.2, "Name ": "Ringo "},
    ]
)

# or from CSV:
from io import StringIO

csv_file = StringIO(
    """ growth ,Name
.5,Paul
.7,George
1.2, Ringo """
)
pd.read_csv(csv_file)


# instantiate a DF from a numpy array:
import numpy as np

np.random.seed(42)
np_df = pd.DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])


# sum the rows:
df.sum(axis=0)
# sum the columns:
df.sum(axis=1)

# spelling out the axis makes it easier to read:
df.sum(axis="columns")
df.sum(axis="index")

# rows/index
df.axes[0]
# columns
df.axes[1]
