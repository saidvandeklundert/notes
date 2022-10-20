import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)


# melt decreases the width of the DF and increases the heigth:
# get a row with name and city for every py-score:
df.melt(id_vars=["name", "city"], value_vars=["py-score"])
# get a row with name and city for every py-score AND for every age:
df.melt(id_vars=["name", "city"], value_vars=["age", "py-score"])

# put age and py-score in 1 column named yolo:
df.melt(
    id_vars=["name", "city"],
    value_vars=["age", "py-score"],
    var_name="age-score",
    value_name="age-score-value",
)
