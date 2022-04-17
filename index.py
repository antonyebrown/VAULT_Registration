import os
import json

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_design_kit as ddk

from app import app, server
from apps import app_main, app_registration, app_viewreg, app_courseinfo


def header():
    menu = [dcc.Link("Home", href=app.get_relative_path("/")),
            dcc.Link("Registration", href=app.get_relative_path("/registration")),
            dcc.Link("View Registrations", href=app.get_relative_path("/view")),
            dcc.Link("Course Info", href=app.get_relative_path("/courseinfo")),
            dcc.Link("VAULT (AF Data Lab)", href= "https://afdatalab.af.mil/")]

    return ddk.Header(
        style={"height": "80px", "margin-bottom": "0%"},
        children=[
            ddk.Logo(src=app.get_asset_url("vault.png"), style={"height": "60px"}),
            ddk.Title("VAULT 101 Course Registration"),
            ddk.Menu(children=menu),
        ],
    )


app.layout = ddk.App(
    [
        header(),
        html.Div(id="content"),
        dcc.Location(id="url", refresh=False),
        dcc.Store(
            id="store-main"
        ),  # For sharing data between callbacks, refer to callback in app_main.py and app_receiver.py
    ]
)


@app.callback(Output("content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    page_name = app.strip_relative_path(pathname)
    if not page_name:
        return app_main.layout()
    elif page_name == "registration":
        return app_registration.layout()
    elif page_name == "view":
        return app_viewreg.layout()
    elif page_name == "courseinfo":
        return app_courseinfo.layout()
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)

