"""
The app displays a radio button and a text field.

The content of the text field is controlled by the input of the radio button.

This is done using the @callback decorator.

There, the 'Input' refers to the 'dcc.RationItems' id and the output
 refers to the 'dcc.Markdown' id.

The callback function can do anything with the radio button input. In
 this case, it is merely displaying the value.
"""
from dash import Dash, dcc, html, Output, Input, callback


app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.RadioItems(
            options=["region", "count", "vendor"], value="region", id="radio-button"
        ),
        dcc.Markdown(children="", id="text-on-web-page"),
    ]
)


@callback(
    Output(component_id="text-on-web-page", component_property="children"),
    Input(component_id="radio-button", component_property="value"),
)
def update_text(
    radio_button_value: str,
):
    """Value is directly passed to the 'text-on-web-page' id."""
    return f"The selected button is: {radio_button_value}"


if __name__ == "__main__":
    app.run(port=8050)
