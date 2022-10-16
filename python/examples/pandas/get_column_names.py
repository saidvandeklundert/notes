import pandas as pd

df = pd.read_csv("101_py_csv_output.csv", index_col=0)

print(df)
# new column with default value
df = df.rename(columns={"age": "AGE", "city": "CITY"})
print(df)
for col in df.columns:
    print(col)
