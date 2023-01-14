"""
>>> df = bf.q.namedStructures().answer().frame()
>>> df.to_csv("named_structure.csv")
docker cp batfish:named_structure.csv named_structure.csv
"""
import pandas as pd

df = pd.read_csv("named_structure.csv")

# get array of hostnames in df:
df["Node"].values
# show 2 columns
df[["Node", "Structure_Type"]]
