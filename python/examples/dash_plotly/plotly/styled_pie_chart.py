import plotly.graph_objects as go
from pydantic import BaseModel


class Region(BaseModel):
    name: str
    count: int


region_data = [
    Region(name="tok", count=100),
    Region(name="ams", count=2039),
    Region(name="fra", count=244),
    Region(name="dub", count=3434),
    Region(name="dal", count=3456),
]


colors = ["blue", "grey", "lightblue", "lightgreen"]

fig = go.Figure(
    data=[
        go.Pie(
            labels=["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"],
            values=[4500, 2500, 1053, 500],
        )
    ]
)
fig.update_traces(
    hoverinfo="label+percent",
    textinfo="value",
    textfont_size=20,
    marker=dict(colors=colors, line=dict(color="#000000", width=2)),
)
fig.show()


names = [region.name for region in region_data]
values = [region.count for region in region_data]
fig = go.Figure(
    data=[
        go.Pie(
            labels=names,
            values=values,
        )
    ]
)
fig.update_traces(
    hoverinfo="label+percent",
    textinfo="value",
    textfont_size=20,
    marker=dict(colors=colors, line=dict(color="#000000", width=2)),
)
fig.show()
fig.write_html("output/styled_pie_chart.html")
