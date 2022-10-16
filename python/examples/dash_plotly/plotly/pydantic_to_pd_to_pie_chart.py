import plotly.express as px
from pydantic import BaseModel
import pandas as pd


class Region(BaseModel):
    name: str
    count: int


regions = [
    Region(name="tok", count=100),
    Region(name="ams", count=2039),
    Region(name="fra", count=244),
    Region(name="dub", count=3434),
    Region(name="dal", count=3456),
]

df = pd.DataFrame([model.dict() for model in regions])

fig = px.pie(df, values="count", names="name", title="Device per datacenter")
fig.show()
fig.write_html("styled_pie_chart.html")
