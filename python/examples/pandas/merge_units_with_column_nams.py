import pandas as pd
import numpy as np


units = pd.read_csv("data\\nutrition.csv")

#####
# iterating the frame
#####

# iterate the colum names:
for k in units:
    print(k)

# iterate the columns and print the series for that column:
for k in units:
    print(units[k])


# prints units
for k in units:
    print(units[k].at[0])


units.replace("", np.nan).dropna(axis=1)
for k in units:
    print(units[k].at[0])


mapper = {k: units[k].at[0] for k in units}

units.rename(columns=mapper, inplace=True)
