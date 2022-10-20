"""
Module with extensive functionality for working with tabular data.
"""
import pandas as pd

# read from csv and use the first column as index:
df = pd.read_csv("101_py_csv_output.csv", index_col=0)
df
"""
       name         city  age  py-score
101  Xavier  Mexico City   41      88.0
102     Ann      Toronto   28      79.0
103    Jana       Prague   33      81.0
104      Yi     Shanghai   34      80.0
105   Robin   Manchester   38      68.0
106    Amal        Cairo   31      61.0
107    Nori        Osaka   37      84.0
"""
df.loc[101]
"""
name             Xavier
city        Mexico City
age                  41
py-score           88.0
Name: 101, dtype: object
"""
df.loc[101].name
df.loc[101].age
