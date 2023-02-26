import pandas as pd
import numpy as np

# by default, Pandas will generate an index:
df = pd.read_csv("data\movies.csv")


# to check the types in the frame:
df.info()

# replacing something straightforward:
df.replace(to_replace="Fox", value="FOX")


# replace using a regex (turn Fox into FOXY):
df.replace(to_replace=".*ox.*", value="FOXY", regex=True)

# remove the $ from the gross colunm:
df.replace(to_replace="[$]", value="", regex=True)

# remove the digits from a column containing integer values:
df["Year"].astype(str).replace(to_replace="20", value="222", regex=True)
