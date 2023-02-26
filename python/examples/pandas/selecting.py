import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)

# entire thing:
df

###
# columns
###


# name column:
df["name"]
# name and py-score column (returns new df):
df[["name", "py-score"]]

# also determine what colums are selected:
df[:, ["name", "py-score"]]

# reset index:
df.reset_index(inplace=True)
# set index:
df.reset_index()
df.set_index("name")
df.set_index("name", inplace=True)


###
# rows
###

# select row by label (will return multiples if multiples match):
df.loc["Anne"]  # returns a series
df.loc["Anne"].age  # returns the field
df.loc["Anne"]["age"]  # also returns the age

# multiple labels:
df.loc[["Anne", "Jan"]]
df.loc[["Anne", "Jan"]].age
df.loc[["Anne", "Jan"], "age"]

# select row by index:
df.iloc[1]
