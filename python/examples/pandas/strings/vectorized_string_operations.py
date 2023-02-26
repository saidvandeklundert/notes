import pandas as pd
import numpy as np

df = pd.read_csv("2017BostonMarathonTop1000.csv")
df.info(memory_usage="deep")

df.head()

# getting the length of the column:
len(df.Name)

# getting the lenght of every item in the column,
# using a vecotrized string operation:
df.Name.str.len()

# many vectorized string operations are very similar to Python
# string methods:
df.Name.str.strip()
df.Name.str.strip().str.startswith("K")
df.Name.str.strip().str.upper()
df.Name.str.upper()
df.Name.str.lower()
df.Name.str.swapcase()
df.Name.str.title()
df.Name.str.capitalize()

# find
df.Name.str.find("Su")
df.Name.str.rfind("Su")  # start searching from the right
df.Name.str.find("Andy").value_counts()


df.Name.iloc[0]  # ' Kirui, Geoffrey '
df.Name.str.strip().iloc[0]  # 'Kirui, Geoffrey'


df.Name.str.split(",")
df.Name.str.split(",").str.get(0)  # get the first element of the list in every row
