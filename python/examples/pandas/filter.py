"""
Module with extensive functionality for working with tabular data.
"""
import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)


# filter by column name:
df.filter(items=["name", "city"])

# show the name colum where the age is above 40:
df["name"].where(df["age"] > 40)
# show all columns for rows where age is above 40:
df.where(df["age"] > 40)
# show all columns for rows where age is above 40, drop all empty rows:
df.where(df["age"] > 40).dropna()


# filter by column name were the age is above 35:
df.filter(items=["name", "city", "age"]).where(df["age"] > 35)
df.filter(items=["name", "city", "age"]).where(df["age"] > 35).dropna()


# show booleans for matches in a column:
df["city"] == "Netherlands"

# use the boolean array to select what columns to display:
bool_array = df["city"] == "Netherlands"
df[bool_array]
# or shorthand:
df[df["city"] == "Netherlands"]


# select rows and use AND on 2 conditions:
bool_array_1 = df["city"] == "Netherlands"
bool_array_2 = df["gender"] == "f"
df[bool_array_1 & bool_array_2]

# select rows and use OR on 2 conditions:
df[bool_array_1 | bool_array_2]

# select based on values:
df["py-score"] > 80
df["py-score"].between(60, 90)

less_then_80 = df["py-score"] > 80
df[less_then_80]

# divide into the 2 genders and then sum the py-score column
# for the genders (makes no sense, but think product categories here!)
df.groupby("gender")["py-score"].sum()
df.groupby("gender")["py-score"].sum().sort_values(ascending=False)
# averge m and f score:
df.groupby("gender")["py-score"].mean()


# contains
contains_an = df.name.str.lower().str.contains("an")
df[contains_an]
