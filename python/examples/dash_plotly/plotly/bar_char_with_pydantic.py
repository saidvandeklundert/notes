import plotly.express as px
from pydantic import BaseModel


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

fig = px.bar(
    x=[region.name for region in regions], y=[region.count for region in regions]
)
fig.show()
