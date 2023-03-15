import pandas as pd


df = pd.read_csv("vehicles.csv.zip")

# show missing
df.isna()

# show missing for specific column:
df[df.startStop.isna()]

# drop duplicates
df.drop_duplicates(subset="make")
df.drop_duplicates(subset="make", keep="last")
