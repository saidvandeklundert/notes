from dash import Dash, dcc, html
import plotly.express as px
from pydantic import BaseModel
import pandas as pd
from dash import Dash, dcc, html, Output, Input, callback


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

# draw the initial figure:
df = pd.DataFrame([model.dict() for model in regions])


def draw_pie_chart(df: pd.DataFrame):
    return px.pie(df, values="count", names="name", title="Device per region")


# the app
button_options = [region.name for region in regions]

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Checklist(button_options, [], id="check-list"),
        dcc.Graph(figure=draw_pie_chart(df), id="my-graph"),
    ]
)


# tying the checklist to the drawing of the graph:
@callback(
    Output(component_id="my-graph", component_property="figure"),
    Input(component_id="check-list", component_property="value"),
    prevent_initial_call=True,
)
def pie_chart(
    items: list[str],
):

    df = pd.DataFrame([region.dict() for region in regions if region.name in items])
    return draw_pie_chart(df)


if __name__ == "__main__":
    app.run(port=8050)
