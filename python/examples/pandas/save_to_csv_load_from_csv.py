import plotly.express as px
import pandas as pd

df = px.data.medals_long()
df.to_csv("data.csv")


df2 = pd.read_csv("data.csv")
df3 = pd.read_csv("data.csv", index_col=0)
