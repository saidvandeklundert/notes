import pandas as pd

p_df = pd.read_csv("101_py_csv_output.csv", index_col=0)

print(p_df)

p_df.drop(labels=[107, 105], inplace=True)
print(p_df)
