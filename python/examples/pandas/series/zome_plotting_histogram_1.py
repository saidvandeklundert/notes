import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline
alta_df = pd.read_csv("alta-noaa-1980-2019.csv")
dates = pd.to_datetime(alta_df.DATE)

snow = alta_df.SNOW.rename(dates)

snow.plot.hist()
plt.show()
